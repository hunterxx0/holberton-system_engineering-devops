#!/usr/bin/python3
""" https://www.reddit.com/r/ """
from requests import get


def top_ten(subreddit):
    res = get('https://www.reddit.com/r/{}/hot.json'
              .format(subreddit), headers={'User-Agent': 'hunter0xx'},
              allow_redirects=False, params={'limit': 10}).json()
    if res and res.get('data'):
        for x in res.get('data').get('children'):
            print('{}'.format(x.get('data').get('title')))
    else:
        print(None)
