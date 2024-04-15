#!/usr/bin/python3
"""class definition of a State"""

from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

myMD = MetaData()
Base = declarative_base(metadata=myMD)


class State(Base):
    """Class state"""
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
