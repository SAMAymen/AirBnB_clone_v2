#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, DateTime, create_engine, ForeignKey
from sqlalchemy.orm import relationship
import models



class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="delete")
    
    @property
    def cities(self):
            """cities list
            """
            result = []
            for j, i in models.storage.all(models.city.City).items():
                if (i.state_id == self.id):
                    result.append(i)
            return result   