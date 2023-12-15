#!/usr/bin/python3
''' This is all about manipulation of database in python'''

if __name__ == '__main__':
    import MySQLdb
    import sys

    cn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    curs = cn.cursor()
    curs.execute("SELECT * FROM states ORDER BY id ASC")
    _rows = curs.fetchall()
    for res in _rows:
        print(res)
    curs.close()
    cn.close()
