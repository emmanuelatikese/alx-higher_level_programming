#!/usr/bin/python3
''' This is all about sql injection'''

if __name__ == '__main__':
    import sys
    import MySQLdb

    cn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    curs = cn.cursor()
    curs.execute("SELECT * FROM states WHERE name='{}' ORDER BY id ASC"
                 .format(sys.argv[4]))
    _rows = curs.fetchall()
    for res in _rows:
        print(res)
    curs.close()
    cn.close()
