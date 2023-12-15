#!/usr/bin/python3

'''This is all about filter'''

if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    cn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    curs = cn.cursor()
    curs.execute("SELECT * FROM states ORDER BY id ASC")
    curs.execute("SELECT * FROM states WHERE name LIKE 'N%'")

    _row = curs.fetchall()

    for x in _row:
        print(x)
    curs.close()
    cn.close()
