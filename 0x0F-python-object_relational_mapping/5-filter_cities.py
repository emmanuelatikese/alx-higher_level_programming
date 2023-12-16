#!/usr/bin/python3

"""This is another script for manipulation of mysql 2"""

if __name__ == '__main__':

    from sys import argv
    import MySQLdb

    my_con = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                             passwd=argv[2], db=argv[3], charset="utf8")

    ex = my_con.cursor()

    ex.execute("SELECT cities.name FROM cities\
                JOIN states ON cities.state_id = states.id\
                WHERE states.name ='{}';".format(argv[4]))
    pr = ex.fetchall()

    for ned in range(len(pr)):
        print(" ", end="") if ned != 0 else ''
        print("{}".format(pr[ned][0]), end="")
        print(",", end="") if ned < len(pr) - 1 else ''
    print('\n') 
    ex.close()
    my_con.close()
