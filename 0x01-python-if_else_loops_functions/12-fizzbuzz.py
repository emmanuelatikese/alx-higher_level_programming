#!/usr/bin/python3
def fizzbuzz():
    for n in range(1, 101):
        if n % 3 == 0 and n % 5 != 0 :
            ans = 'Fizz'
        elif n % 5 == 0 and n % 3 != 0:
            ans = 'Buzz'
        elif n % 5 == 0 and n % 3 == 0:
            ans = 'FizzBuzz'
        else:
            ans = str(n)
        if n < 101:
            ans = ans + " "
        print(ans, end='')
