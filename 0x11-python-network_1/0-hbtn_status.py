#!/usr/bin/python3
"""This is all about urllib norhing else"""
if __name__ == '__main__':
    import urllib.request

    url = "https://alx-intranet.hbtn.io/status"
    req = urllib.request.Request(url)

    with urllib.request.urlopen(req) as f:
        page = f.read()
    print('Body response:')
    print('\t- type: %s' % type(page))
    print('\t- content: %s' % page)
    print('\t- utf8 content: %s' % page.decode('utf-8'))
