#!/usr/bin/python3
for a in range(0, 100):
    if a < 9:
        a = "0" + str(a)
    if int(a) // 10 > int(a) % 10 or int(a) // 10 == int(a) % 10:
        continue
    if int(a) < 89:
        a = str(a) + ',' + " "
    print(('{:}').format(str(a)), end='')
print('\n')
