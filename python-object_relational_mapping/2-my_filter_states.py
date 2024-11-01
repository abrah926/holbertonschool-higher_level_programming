#!/usr/bin/python3
"""
Displays all values in the states table where the name matches the input argument.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Retrieve MySQL credentials and database name from arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]  # The state name to search for

    # Connect to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=db_name
    )

    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # Create the SQL query using format to insert the state_name safely
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(
        state_name)

    # Execute the SQL query
    cursor.execute(query)

    # Fetch and print each row in the result set
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close the cursor and the database connection
    cursor.close()
    db.close()
