#!/usr/bin/python3
'''We working on the request lib'''

if __name__ == '__main__':
    import requests
    req = requests.get("https://alx-intranet.hbtn.io/status")
    print('Body response:')
    print('    - type: {}'.format( type(req.text)))
    print('    - content: {}'.format(req.text))
