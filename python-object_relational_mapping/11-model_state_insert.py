#!/usr/bin/python3
"""
This script connects to a MySQL database using SQLAlchemy,
creates a new State object with the name "Louisiana," adds it
to the session, commits the transaction, and prints the ID of
the newly created state.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

mysql_username = sys.argv[1]
mysql_password = sys.argv[2]
database_name = sys.argv[3]

mysql_db_url = f"mysql+mysqldb://{mysql_username}:{mysql_password}@localhost:3306/{database_name}"

engine = create_engine(mysql_db_url)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

new_state = State(name="Louisiana")
session.add(new_state)
session.commit()

session.close()

print(new_state.id)

if __name__ == "__main__":
    pass
