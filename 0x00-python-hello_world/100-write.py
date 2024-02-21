#!/usr/bin/python3
import sys
s = "and that piece of art is useful - Dora Korpar, 2015-10-19"
lt = s.split(" ")
for i in range(len(lt)):
    if i < len(l) and i != 0:
        sys.stderr.write(" ")
    sys.stderr.write(lt[i])
sys.stderr.write('\n')
sys.exit(1)
