#!/usr/bin/python3
'''looking for something in the header'''

if __name__ == "__main__":
    from urllib.request import Request, urlopen
    from sys import argv

    req = Request(argv[1])

    with urlopen(req) as f:
        print(f.info()['X-Request-Id'])
