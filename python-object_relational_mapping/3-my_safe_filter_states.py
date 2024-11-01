#!/usr/bin/python3
"""
Displays all values in the states table where the name matches the input argument, safely from SQL injection.
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

    state = sys.argv[4]

    cur = db.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(query, (state,))

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
