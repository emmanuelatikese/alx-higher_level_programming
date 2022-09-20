#!/usr/bin/python3
for a in range(0, 100):
    if a < 9:
        a = "0" + str(a)
    if int(a) < 99:
        a = str(a) + ','+ " "
    print(('{:}').format(str(a)), end='')
print('\n')
