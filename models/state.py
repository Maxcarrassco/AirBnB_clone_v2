#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state')

    @property
    def cities(self):
        """Return the list of cities whose state_id equal state.id."""
        from models import storage
        city_dict = storage.all(City)
        cities_out = []

        for k in city_dict:
            state_id = k[k.find('.') + 1:]
            if state_id == self.id:
                cities_out.append(city_dict[k])
        return cities_out
