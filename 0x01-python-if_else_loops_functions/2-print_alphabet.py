#!/usr/bin/python3
b = ""
for a in range(ord("A"), ord("Z")+1):
    b = b + chr(a).lower()
print("{}".format(b))
