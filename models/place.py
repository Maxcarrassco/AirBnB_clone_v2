#!/usr/bin/python3
""" Place Module for HBNB project """
from sqlalchemy.sql.schema import Table
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship
from models.review import Review


place_amenity_table = Table(
        "place_amenity",
        Base.metadata,
        Column("place_id", String(60), ForeignKey(
            'places.id'), primary_key=True),
        Column("amenity_id", String(60), ForeignKey(
            'amenities.id'), primary_key=True))


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'))
    user_id = Column(String(60), ForeignKey('users.id'))
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    reviews = relationship('Review', backref='place')
    amenity_ids = []
    amenities = relationship(
            "Amenity",
            secondary="place_amenity",
            viewonly=True)

    @property
    def reviews(self):
        """
        Returns the list of Review instances.
        With place_id equals to the current Place.id.
        """
        from models import storage
        objs = []
        for _, v in storage.all(Review).items():
            if self.id == v.place_id:
                objs.append(str(v))
        return objs

    @property
    def amenities(self):
        """
        Returns the list of Amenity instances based on the attribute.
        Amenity_ids that contains all Amenity.id linked to the Place.
        """
        from models import storage
        from models.amenity import Amenity

        objs = []
        for _, v in storage.all(Amenity).items():
            if v.id in self.amenity_ids:
                objs.append(str(v))
        return objs

    @amenities.setter
    def amenities(self, obj):
        """
        Add an Amenity.id to the attribute amenity_ids.
        Only Amenity object, otherwise, do nothing.
        """
        from models.amenity import Amenity

        if type(obj) is not Amenity:
            return
        self.amenity_ids.append(obj.id)
