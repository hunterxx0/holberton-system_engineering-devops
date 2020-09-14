#!/usr/bin/python3
""" Fetches https://intranet.hbtn.io/status """
import csv
from json import loads
from requests import get
from sys import argv


if __name__ == "__main__":
    user_id = eval(argv[1])
    res = get('https://jsonplaceholder.typicode.com/todos').text
    user = get('https://jsonplaceholder.typicode.com/users/{}'
               .format(user_id)).text
    dict_list = loads(res)
    result = []
    for dic in dict_list:
        if dic['userId'] == user_id:
            result.append(dic)
    username = eval(user).get('username')
    with open('{}.csv'.format(user_id), mode='w', encoding='utf-8') as f:
        w = csv.writer(f)
        for dic in result:
            ll = []
            ll.append(user_id)
            ll.append(username)
            ll.append(dic['completed'])
            ll.append(dic['title'])
            w.writerow(ll)
