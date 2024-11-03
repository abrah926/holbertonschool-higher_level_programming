#!/usr/bin/python3
"""Define a State class that links to the states table in the MySQL database."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create a declarative base instance
Base = declarative_base()


class State(Base):
    """State class that links to the states table in the database."""

    __tablename__ = 'states'  # Name of the table in the database

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

    def __repr__(self):
        return f"<State(id={self.id}, name='{self.name}')>"
