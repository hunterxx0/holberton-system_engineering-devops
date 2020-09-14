#!/usr/bin/python3
""" Fetches https://intranet.hbtn.io/status """
from json import loads, dumps
from requests import get


if __name__ == "__main__":
    res = get('https://jsonplaceholder.typicode.com/todos').text
    all_users = {}
    dict_list = loads(res)
    for i in range(1, 11):
        user = get('https://jsonplaceholder.typicode.com/users/{}'
                   .format(i)).text
        result = []
        username = eval(user).get('username')
        for dic in dict_list:
            if dic['userId'] == i:
                tmp = {
                    "task": dic['title'],
                    "completed": dic['completed'],
                    "username": username
                }
                result.append(tmp)
        all_users[i] = result
    with open('{}.json'.format('todo_all_employees'),
              mode='w', encoding='utf-8') as f:
        f.write(dumps(all_users))
