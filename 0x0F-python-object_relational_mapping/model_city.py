#!/usr/bin/python3
"""Defines class City which links to the MySQL table states."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State

Base = declarative_base()


class City(Base):
    """Represents a city for a MySQL database."""

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, unique=True,)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
