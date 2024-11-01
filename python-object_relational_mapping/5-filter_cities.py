#!/usr/bin/python3

"""
Script that takes in the name of a state
as an argument and lists all cities of that state
from the database hbtn_0e_4_usa.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Ensure the correct number of arguments is provided
    if len(sys.argv) != 5:
        print("Usage: ./5-filter_cities.py <mysql_username> <mysql_password> <database_name> <state_name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cur = db.cursor()

    # Parameterized query to prevent SQL injection
    query = """SELECT cities.name
                FROM states
                INNER JOIN cities ON states.id = cities.state_id
                WHERE states.name = %s
                ORDER BY cities.id ASC"""
    cur.execute(query, (state_name,))

    # Fetch and print results
    rows = cur.fetchall()
    print(", ".join([row[0] for row in rows]))

    # Cleanup
    cur.close()
    db.close()
