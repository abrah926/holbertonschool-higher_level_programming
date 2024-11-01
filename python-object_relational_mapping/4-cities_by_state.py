#!/usr/bin/python3

"""
Script that lists all cities from the database.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Ensure correct number of arguments
    if len(sys.argv) != 4:
        print("Usage: ./4-cities_by_state.py <mysql_username> <mysql_password> <database_name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cur = db.cursor()
    query = """SELECT cities.id, cities.name, states.name
                FROM states
                INNER JOIN cities
                ON states.id = cities.state_id
                ORDER BY cities.id ASC"""
    cur.execute(query)

    rows = cur.fetchall()
    for row in rows:
        print(row[1], row[2])  # Printing city name and state name

    cur.close()
    db.close()
