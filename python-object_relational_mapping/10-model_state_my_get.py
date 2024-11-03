#!/usr/bin/python3
"""
A script that prints the State object with the name passed as an argument
from the database hbtn_0e_6_usa. It connects to a MySQL server running
on localhost at port 3306 and ensures SQL injection safety. If the state
is not found, it displays 'Not found'.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    if len(sys.argv) != 5:
        print("Usage: ./10-model_state_my_get.py <mysql_username> <mysql_password> <database_name> <state_name>")
        return

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    mysql_db_url = f"mysql+mysqldb://{mysql_username}:{mysql_password}@localhost:3306/{database_name}"
    engine = create_engine(mysql_db_url)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == state_name).first()

    if state:
        print(state.id)
    else:
        print("Not found")


if __name__ == "__main__":
    main()
