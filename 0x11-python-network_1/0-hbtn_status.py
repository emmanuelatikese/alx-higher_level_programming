#!/usr/bin/python3
"""This is all about urllib norhing else"""
import urllib.request

if __name__ == '__main__':
    url = "https://alx-intranet.hbtn.io/status"
    req = urllib.request.Request(url)
    result = """Body response:
    - type: {}
    - content: {}
    - utf8 content: {}"""

    with urllib.request.urlopen(req) as f:
        page = f.read()
    print(result.format(type(page), page, page.decode()))
