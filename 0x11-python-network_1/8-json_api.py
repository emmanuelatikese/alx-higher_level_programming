#!/usr/bin/python3
'''This is all about search'''

if __name__ == "__main__":
    from requests import get, post
    from sys import argv

    lt = argv[1] or ''
    try:
        req = post('http://0.0.0.0:5000/search_user', data={'q': lt}).json()
    except ValueError:
        print('Not a valid JSON')
    else:
        if req:
            print('[{}] {}'.format(req.get('id'), req.get('name')))
        else:
            print('No result')
