#!/usr/bin/python3
for a in range(97, 123):
    if ord('q') == a or ord('e') == a:
        continue
    print("{:c}".format(a),end= "")
