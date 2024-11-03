#!/usr/bin/python3

"""
Script that takes in the name of a state
as an argument and lists all cities of that state,
in the database.
"""

import MySQLdb
import sys

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cur = db.cursor()
    state_name = sys.argv[4]
    query = """SELECT cities.name
                FROM states
                INNER JOIN cities
                ON states.id = cities.state_id
                WHERE states.name = %s
                ORDER BY cities.id ASC"""
    cur.execute(query, (state_name,))

    rows = cur.fetchall()
    print(", ".join([row[0] for row in rows]))

    cur.close()
    db.close()
