#!/usr/bin/python3
'''making a post request'''

if __name__ == '__main__':
    import requests
    from sys import argv

    req = requests.post(argv[1], data={'email': argv[2]})
    print(req.text)
