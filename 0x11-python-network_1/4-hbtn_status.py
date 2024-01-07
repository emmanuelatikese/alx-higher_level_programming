#!/usr/bin/python3
'''We working on the request lib'''
import requests

if __name__ == '__main__':
    req = requests.get("https://alx-intranet.hbtn.io/status")
    print('Body response:')
    print('    - type: {}'.format(type(req.text)))
    print('    - content: {}'.format(req.text))
