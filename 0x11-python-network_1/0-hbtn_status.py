#!/usr/bin/python3
"""This is all about urllib norhing else"""
from urllib.request import Request, urlopen

url = "https://alx-intranet.hbtn.io/status"

req = Request(url)
result = """Body response:
    - type: {}
    - content: {}
    - utf8 content: {}"""

with urlopen(req) as f:
    page = f.read()
print(result.format(type(page), page, page.decode()))
