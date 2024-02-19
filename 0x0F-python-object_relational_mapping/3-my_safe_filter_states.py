#!/usr/bin/python3
"""A script that takes in arguments and displays all values
in the states table safe from MySQL injections."""

import MySQLdb
import sys


def main():

    username, password, database, state_name = sys.argv[1],
    sys.argv[2], sys.argv[3], sys.argv[4]

    # Connect to the MySQL database
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)

    # Create a cursor object to execute SQL queries
    cur = db.cursor()

    # SQL query using placeholders for parameters
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

    # Execute the query with user input as parameter to prevent SQL injection
    cur.execute(query, (state_name,))

    # Fetch all results
    states = cur.fetchall()

    # Print each state that matches the input argument
    for state in states:
        print(state)

    # Close cursor and database connection
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
