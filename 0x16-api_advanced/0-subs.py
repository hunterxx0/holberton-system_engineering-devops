#!/usr/bin/python3
""" https://www.reddit.com/r/ """
from requests import get


def number_of_subscribers(subreddit):
    """ Returns the number of subscribers """
    res = get('https://www.reddit.com/r/{}/about.json'
              .format(subreddit), headers={'User-Agent': 'hunter0xx'}).json()
    if res and res.get('data'):
        return (res.get('data').get('subscribers'))
    else:
        return 0
