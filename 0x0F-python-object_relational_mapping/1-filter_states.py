#!/usr/bin/python3
""" lists all states with name starting in N """

import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3])

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states\
                    WHERE BINARY name LIKE 'N%'\
                    ORDER BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
