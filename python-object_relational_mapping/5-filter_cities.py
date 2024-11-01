#!/usr/bin/python3

"""
Script that lists all cities of a specified state from the database hbtn_0e_4_usa.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
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

    # Using a parameterized query to prevent SQL injection
    query = """SELECT cities.name
                FROM cities
                INNER JOIN states ON cities.state_id = states.id
                WHERE states.name = %s
                ORDER BY cities.id ASC"""

    # Execute the query with the state name parameter
    cur.execute(query, (state_name,))

    rows = cur.fetchall()

    # Extract city names from the result set
    city_names = [row[0] for row in rows]

    # Print the city names, joined by a comma
    print(", ".join(city_names))

    cur.close()
    db.close()
