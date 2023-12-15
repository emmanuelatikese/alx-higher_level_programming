#!/usr/bin/python3
import MySQLdb
from sys import argv
''' This is all about manipulation of database in python'''

if __name__ == '__main__':
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM states ORDER BY id ASC")
    _rows = cur.fetchall()
    for res in _rows:
        print(res)
    cur.close()
    conn.close()
