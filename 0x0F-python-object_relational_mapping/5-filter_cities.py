#!/usr/bin/python3
'''
This script takes in name of a state as an argument
and lists all cities of that state using the
database hbtn_0e_4_usa.
'''

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         password=argv[2],
                         database=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities INNER JOIN states ON\
    cities.state_id = states.id WHERE states.name LIKE %(state_name)s\
    ORDER BY cities.id ASC", {'state_name': argv[4]})
    res = cur.fetchall()
    print(', '.join(row[0] for row in res))
    db.close()
