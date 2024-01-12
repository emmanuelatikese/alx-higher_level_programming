#!/usr/bin/python3
'''using of api auth'''
if __name__ == '__main__':

    import requests
    from sys import argv
    username = argv[1]
    password = argv[2]
    req = requests.get('https://api.github.com/users', auth=(username, password))
    res = req.json()
    print(res[0].get('id'))
