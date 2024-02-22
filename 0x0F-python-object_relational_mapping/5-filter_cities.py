#!/usr/bin/python3
"""A script that takes in the name of a state as an argument
and lists all cities of that state safe from SQL injections."""

import MySQLdb
import sys


def main():
        if len(sys.argv) == 5:
        username, password, database, state_name = sys.argv[1], sys.argv[2],
        sys.argv[3], sys.argv[4]
    else:
        print("Usage: ./script.py <mysql username> <mysql password> <database name> <state name>")
        return

    username, password, database = sys.argv[1],
    sys.argv[2], sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)

    cur = db.cursor()

    query = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """
    cur.execute(query, (state_name,))

    rows = cur.fetchall()

    print(", ".join(city[0] for city in cities))

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
