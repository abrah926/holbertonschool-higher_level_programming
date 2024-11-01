#!/usr/bin/python3

"""
Script that takes in arguments and displays all values
in the states table of the database where name matches the argument
but this time is safe from SQL injection.
"""

import MySQLdb
import sys

if __name__ == "__main__":

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cur = db.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(query, (sys.argv[4],))

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
