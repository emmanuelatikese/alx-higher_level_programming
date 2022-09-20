#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = str(number)
if number < 0:
    b = - int(num[len(num) -1])
else:
    b = int(num[len(num) -1])
if b == 0:
    a = f"Last digit of {number} is {b} and is 0"
elif b > 5:
    a =f"Last digit of {number} is {b} and is greater than 5"
else:
    a = f"Last digit of {number} is {b} and is less than 6 and not 0"
print(a)
