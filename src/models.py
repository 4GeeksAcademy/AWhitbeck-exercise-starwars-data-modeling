import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)

    def serialize(self):
        return {
            "user_name": self.user_name,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email
            }

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    rotation_period = Column(String(250), nullable=True)
    orbital_period = Column(String(250), nullable=True)
    diameter = Column(String(250), nullable=True)

    def serialize(self):
        return {
            "name": self.name,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "diameter": self.diameter
            }
    
class Starships(Base):
    __tablename__ = 'starships'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250), nullable=True)
    manufacturer = Column(String(250), nullable=True)
    cargo_capacity = Column(String(250), nullable=False)

    def serialize(self):
        return {
            "name": self.name,
            "model": self.model,
            "manufacturer": self.manufacturer,
            "cargo_capacity": self.cargo_capacity
            }



render_er(Base, 'diagram.png')
