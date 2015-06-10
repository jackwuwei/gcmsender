# -*- coding: utf-8 -*-
__author__ = 'wuwei'

import requests

send_url = 'https://gcm-http.googleapis.com/gcm/send'
api_key = 'API_KEY'

headers = {'Authorization' : 'key='+api_key, 'Content-Type' : 'application/json'}
msg = '{"from" : "Jack", "to": "/topics/global","data": {"message": "This is a GCM Topic Message!"}}'

r = requests.post(send_url, data=msg, headers=headers)
print(r.headers)
print(r.text)