#!/usr/bin/python3
""" Fetches https://intranet.hbtn.io/status """
from json import loads, dumps
from requests import get
from sys import argv


if __name__ == "__main__":
    user_id = eval(argv[1])
    res = get('https://jsonplaceholder.typicode.com/todos').text
    user = get('https://jsonplaceholder.typicode.com/users/{}'
               .format(user_id)).text
    dict_list = loads(res)
    result = []
    username = eval(user).get('username')
    for dic in dict_list:
        if dic['userId'] == user_id:
            tmp = {
                "task": dic['title'],
                "completed": dic['completed'],
                "username": username
            }
            tmp["username"] = username
            result.append(tmp)
    with open('{}.json'.format(user_id), mode='w', encoding='utf-8') as f:
        f.write(dumps({user_id: result}))
