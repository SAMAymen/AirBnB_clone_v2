#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models import storage
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

    @property
    def cities(self):
        """Getter attribute cities that returns the list of City instances with state_id equals State.id"""
        all_cities = storage.all(City)
        state_cities = []
        for city in all_cities.values():
            if city.state_id == self.id:
                state_cities.append(city)
        return state_cities
