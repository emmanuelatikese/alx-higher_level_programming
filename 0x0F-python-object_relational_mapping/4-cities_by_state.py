#!/usr/bin/python3

"""This is another script for manipulation of mysql"""

if __name__ == '__main__':

    from sys import argv
    import MySQLdb

    my_con = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                             passwd=argv[2], db=argv[3], charset="utf8")

    ex = my_con.cursor()

    ex.execute("SELECT cities.id, cities.name, states.name FROM cities\
                JOIN states on cities.state_id = states.id;")
    pr = ex.fetchall()

    for ned in pr:
        print(ned)
    ex.close()
    my_con.close()
