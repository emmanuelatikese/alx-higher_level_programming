#!/usr/bin/python3
'''using of api auth'''
if __name__ == '__main__':
    import requests
    from sys import argv
    username = argv[1]
    password = argv[2]
    req = requests.get('https://api.github.com/user', auth=(username, password))
    res = req.json()
    print(res.get('id'))
