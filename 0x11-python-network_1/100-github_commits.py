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
    for x in res:
        if count < 10:
            author = x['commit']['author']['name']
            print('{}: {}'.format(x['sha'], author))
            count += 1
        else:
            break
