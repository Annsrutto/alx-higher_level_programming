#!/usr/bin/python3
"""A script that takes in the name of a state as an argument
and lists all cities of that state safe from SQL injections."""

import MySQLdb
import sys


def main():

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

    cities = cur.fetchall()

    print(", ".join(city[0] for city in cities))

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
