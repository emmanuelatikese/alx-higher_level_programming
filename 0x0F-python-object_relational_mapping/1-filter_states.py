#!/usr/bin/python3

'''This is all about filter'''

if __name__ == '__main__':
    import MySQLdb
    import sys

    cn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    curs = cn.cursor()
    curs.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    _row = curs.fetchall()
    for new_row in _row:
        print(new_row)
    curs.close()
    cn.close()
