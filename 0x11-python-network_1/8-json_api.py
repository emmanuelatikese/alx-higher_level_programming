#!/usr/bin/python3
'''This is all about search'''

if __name__ == "__main__":
    from requests import get, post
    from sys import argv

    if len(argv) == 2:
        req = get('http://0.0.0.0:5000/search_user')
        if argv[2] in req:
            print('[{}] {}'.format(req['id'], req['name']))
        else:
            print('No result')
    else:
        req = post('http://0.0.0.0:5000/search_user', data={'q': ''})
        print('No result')
