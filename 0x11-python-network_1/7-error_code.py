#!/usr/bin/python3
'''This is all about the errors'''

if __name__ == '__main__':
    import requests
    from sys import argv
    req = requests.get(argv[1])
    print('Error code:', req.status_code)
