#!/usr/bin/python3
'''We posting things out here'''
from urllib.request import Request, urlopen
from urllib.parse import urlencode
from sys import argv

if __name__ == '__main__':
    url = argv[1]
    data = urlencode({'email': argv[2]}).encode('ascii')
    req = Request(url, data)
    with urlopen(req) as f:
        print(f.read())
