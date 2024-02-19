#!/usr/bin/python3
"""A script that lists all cities from the database hbtn_0e_4_usa."""

import MySQLdb
import sys


def main():

    username, password, database = sys.argv[1],
    sys.argv[2], sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)

    cur = db.cursor()

    query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC
    """

    cur.execute(query)

    cities = cur.fetchall()

    for city in cities:
        print(city)

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
