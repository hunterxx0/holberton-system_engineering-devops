#!/usr/bin/python3
""" https://www.reddit.com/r/ """
from json import loads
from requests import get


def recurse(subreddit, hot_list=[], flag=None):
    res = get('https://www.reddit.com/r/{}/hot.json?after={}'
              .format(subreddit, flag), headers={'User-Agent': 'hunter0xx'},
              allow_redirects=False).json()
    if res and res.get('data'):
        for x in res.get('data').get('children'):
            hot_list.append(x.get('data').get('title'))
        flag = res.get('data').get('after')
        if not flag:
            return hot_list
        else:
            return recurse(subreddit, hot_list, flag)
    else:
        return None
