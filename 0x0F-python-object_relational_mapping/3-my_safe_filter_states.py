#!/usr/bin/python3
'''
A script that is free from MySQL Injection.
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
    cur.execute("SELECT * FROM states WHERE name LIKE\
    %(state_name)s ORDER BY id ASC", {'state_name': argv[4]})
    for data in cur.fetchall():
        if data[1] == argv[4]:
            print(data)
    db.close()
