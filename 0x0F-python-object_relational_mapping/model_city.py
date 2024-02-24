#!/usr/bin/python3
"""Defines class City which links to the MySQL table states."""

from sqlalchemy import Column, Integer, String
from model_state import Base, State


class City(Base):
    """Class City representation"""

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
