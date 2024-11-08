#!/usr/bin/python3
"""
A script that lists all State objects that contain the letter 'a'
from the database hbtn_0e_6_usa. It connects to a MySQL server
running on localhost at port 3306 and displays the results in
ascending order by states.id.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    if len(sys.argv) != 4:
        print("Usage: ./9-model_state_filter_a.py <mysql_username> <mysql_password> <database_name>")
        return

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    mysql_db_url = f"mysql+mysqldb://{mysql_username}:{mysql_password}@localhost:3306/{database_name}"
    engine = create_engine(mysql_db_url)
    Session = sessionmaker(bind=engine)
    session = Session()

    states_with_a = session.query(State).filter(
        State.name.like('%a%')).order_by(State.id).all()

    for state in states_with_a:
        print(f"{state.id}: {state.name}")

    session.close()


if __name__ == "__main__":
    main()