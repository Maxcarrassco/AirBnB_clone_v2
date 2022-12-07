#!/usr/bin/python3

"""Database Storage Module."""
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.user import User
from models.amenity import Amenity
from models.state import State
from models.review import Review
import os


class DBStorage:
    """Implement Database related functionality for our backend."""

    __engine = None
    __session = None

    def __init__(self) -> None:
        """Initialize the DBStorage Module."""
        HBNB_MYSQL_USER = os.environ.get('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = os.environ.get('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = os.environ.get('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = os.environ.get('HBNB_MYSQL_DB')
        HBNB_ENV = os.environ.get('HBNB_ENV')

        self.__engine = create_engine(f"""mysql://{HBNB_MYSQL_USER}:{
                HBNB_MYSQL_PWD}@{HBNB_MYSQL_HOST}/{
                HBNB_MYSQL_DB}""", pool_pre_ping=True)
        if HBNB_ENV == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Query on the current database session (self.__session).
        All objects depending of the class name (argument cls).
        """
        # models = [User, State, City, Amenity, Place, Review]
        models = [State, City]
        obj_dict = {}
        if not cls:
            for cls in models:
                for objs in self.__session.query(cls).all():
                    obj = objs.to_dict()
                    key = f"{obj['__class__']}.{obj['id']}"
                    obj_dict[key] = objs

        else:
            for objs in self.__session.query(cls).all():
                obj = objs.to_dict()
                key = f"{obj['__class__']}.{obj['id']}"
                obj_dict[key] = objs
        return obj_dict

    def new(self, obj):
        """Add new object to the database."""
        self.__session.add(obj)

    def save(self):
        """Add commit all changes to the database."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete an object from the database."""
        self.__session = Session(self.__engine)
        if not obj:
            return
        obj = self.__session.query(obj).filter(obj.id == id).first()
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create Session using sessionmaker factory fuction."""
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session)
