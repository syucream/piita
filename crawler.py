# -*- coding: utf-8 -*-
#
# Qiita item crawler
#
# stdin:
# [
#   {"label": 1, "item_id": "AAAA..."},
#   ...
# ]
#
# #=>
#
# stdout:
# [
#   {"label": 1, "body": "item body..."},
#   ...
# ]
#

import json
import sys
import urllib.request

URL = 'https://qiita.com/api/v2/items/'
TOKEN = '<your token>'
HEADERS = {'Authorization': 'Bearer ' + TOKEN}

def get_item(item_id):
    req = urllib.request.Request(url = URL + item_id, headers = HEADERS)
    with urllib.request.urlopen(req) as res:
        return res.read().decode('utf-8')

def get_item_md(item_id):
    rv = json.loads(get_item(item_id))
    return rv['body']

if __name__ == '__main__':
    stdin = sys.stdin.read()
    labels = json.loads(stdin)
    markdowns = [{'label': v['label'], 'body': get_item_md(v['item_id'])} for v in labels]
    print(json.dumps(markdowns))
