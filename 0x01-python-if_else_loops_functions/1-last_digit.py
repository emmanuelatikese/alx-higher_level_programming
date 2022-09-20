#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = str(number)
if int(num[len(num) -1])==0:
    a = "0"
elif int(num[len(num)-1])>5:
    a ="greater than 5"
else:
    a = "less than 6 and not 0"
print(f"Last digit of {number} is {num[len(num)-1]} and is {a}")
