#!/usr/bin/python3
""" Fetches https://intranet.hbtn.io/status """
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
    done = 0
    title_list = []
    for dic in dict_list:
        if dic['userId'] == user_id:
            result.append(dic)
            if dic['completed'] is True:
                done += 1
                title_list.append(dic['title'])
    print("Employee {} is done with tasks({}/{}):"
          .format(eval(user).get('name'), done, len(result)))
    for title in title_list:
        print('\t {}'.format(title))
