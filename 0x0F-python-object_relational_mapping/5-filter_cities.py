#!/usr/bin/python3
"""Lists states from a database"""
import MySQLdb
import sys

if __name__ == "__main__":
    user = sys.argv[1]
    pw = sys.argv[2]
    db = sys.argv[3]
    states = sys.argv[4]
    database = MySQLdb.connect('localhost', user, pw, db, 3306)
    cur = database.cursor()
    cur.execute("""SELECT name FROM cities
              WHERE state_id = (SELECT id FROM states
              WHERE name='{}')
              ORDER BY id""".format(states))
    rows = cur.fetchall()
    cities = list()
    for row in rows:
        cities.append(*row)
    print(', '.join(cities))
    database.close()
