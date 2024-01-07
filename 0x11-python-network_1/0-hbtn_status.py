#!/usr/bin/python3
"""This is all about urllib norhing else"""
if __name__ == '__main__':
    import urllib.request

    url = "https://alx-intranet.hbtn.io/status"
    req = urllib.request.Request(url)

    with urllib.request.urlopen(req) as f:
        page = f.read()
    print('Body response:')
    print('    - type: %s' % type(page))
    print('    - content: %s' % page)
    print('    - utf8 content: %s' % page.decode('utf-8'))
