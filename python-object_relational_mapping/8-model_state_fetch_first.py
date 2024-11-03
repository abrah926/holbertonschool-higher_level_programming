#!/usr/bin/python3

"""
Script that prints the first State object from the database.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    # Get the command-line arguments
    if len(sys.argv) != 4:
        print("Usage: ./8-model_state_fetch_first.py <mysql_username> <mysql_password> <database_name>")
        return

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create the SQLAlchemy engine and session
    mysql_db_url = f"mysql+mysqldb://{mysql_username}:{mysql_password}@localhost:3306/{database_name}"
    engine = create_engine(mysql_db_url)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for the first State object
    first_state = session.query(State).order_by(State.id).first()

    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")


if __name__ == "__main__":
    main()
