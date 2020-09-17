#!/usr/bin/python3
""" https://www.reddit.com/r/ """
from requests import get


def count_words(subreddit, word_list, flag=None, c=0, idx=0, ll={}):
    """ Returns a list the titles of all hot articles for a subreddit. """
    res = get('https://www.reddit.com/r/{}/hot.json?after={}'
              .format(subreddit, flag), headers={'User-Agent': 'hunter0xx'},
              allow_redirects=False).json()
    if res and res.get('data'):
        for x in res.get('data').get('children'):
            if word_list[idx].lower() in x.get('data').get('title').lower():
                c += 1
        flag = res.get('data').get('after')
        if not flag and idx != len(word_list) - 1:
            if c != 0:
                ll[word_list[idx]] = c
            return count_words(subreddit, word_list, None, 0, idx + 1, ll)
        elif not flag and idx == len(word_list) - 1:
            if c != 0:
                ll[word_list[idx]] = c
            if len(ll) > 0:
                a = sorted(ll.items(), key=lambda x: x[1], reverse=True)
                for x, y in a:
                    print("{}: {}".format(x, y))
            return
        else:
            return count_words(subreddit, word_list, flag, c, idx)
