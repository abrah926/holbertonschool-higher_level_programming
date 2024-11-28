#!/usr/bin/python3

"""
Script that changes the name of a State object
from the database.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                           .format(username, password, 'localhost', database))

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).where(State.id == 2).first()
    state.name = 'New Mexico'
    session.add(state)
    session.commit()

    session.close()
