#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
    from sys import argv, exit

    def fun1():
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    def fun2():
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    if len(argv[1:]) != 3 or len(argv) == 0:
        print(fun1())
    else:
        operator = ['+', '-', '*', '/']
        a = int(argv[1])
        b = int(argv[3])
        c = 0
        if argv[2] in operator:
            if argv[2] == '+':
                c = add(a, b)
                print("{} + {} = {}".format(a, b, c))
            elif argv[2] == '-':
                c = sub(a, b)
                print("{} - {} = {}".format(a, b, c))
            elif argv[2] == '*':
                c = mul(a, b)
                print("{} * {} = {}".format(a, b, c))
            else:
                c = div(a, b)
                print("{} / {} = {}".format(a, b, c))
        else:
            print(fun2())
