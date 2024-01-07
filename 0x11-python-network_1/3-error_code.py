#!/usr/bin/python3
'''This is all about the error we don't want.'''
if __name__ == '__main__':
    from urllib.request import Request, urlopen
    from urllib.error import HTTPError
    from sys import argv

    try:
        req = Request(argv[1])
    except HTTPError as e:
        print('Error code:', e.code)
    else:
        with urlopen(req) as f:
            print(f.read().decode('utf-8'))
