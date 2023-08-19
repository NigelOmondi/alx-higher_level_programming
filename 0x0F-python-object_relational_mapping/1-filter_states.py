#!/usr/bin/python3
'''
List states with name starting
with N, from hbtn_0e_usa database.
'''

import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3])
    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC;")
    for row in cur.fetchall():
        if row[1][0] == 'N':
            print(row)
    db.close()
