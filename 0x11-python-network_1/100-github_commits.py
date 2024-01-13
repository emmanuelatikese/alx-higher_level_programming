#!/usr/bin/python3
'''This is all about the commits'''

if __name__ == '__main__':
    import requests
    from sys import argv
    v1 = argv[1]
    v2 = argv[2]
    req = requests.get('https://api.github.com/repos/{}/{}/commits'
                       .format(v1, v2))
    res = req.json()
    count = 0
    try:
        for x in range(0, 10):
            sha = res[x].get('sha')
            author = res[x].get('commit').get('author').get('name')
            print('{}: {}'.format(sha, author))
    except IndexError:
        pass
