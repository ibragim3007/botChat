#!/usr/bin/env python

import json

from urllib.request import urlopen
from urllib.parse import urlencode, quote_plus


def token(login, password):
    payload = {'login': login, 'password': password}
    params = urlencode(payload, quote_via=quote_plus)
    url = 'http://paraphraser.ru/token?{0}'.format(params)
    return json.loads(urlopen(url).read().decode('utf-8'))['token']

def send(payload):
    params = urlencode(payload, quote_via=quote_plus)
    url = 'http://paraphraser.ru/api?{0}'.format(params)
    try:
        return json.loads(urlopen(url).read().decode('utf-8'))
    except Exception as err:
        return json.loads(err.read().decode('utf-8'))


def activeateFindVectors(str):
    str = str[0:89]
    return getVector(str.partition(' ')[2], 5)

token = token('ibragimlol', 'ibra30072002')


def getVector(str, top):
    if token is not None:
        result = send({
            'c': 'vector',
            'query': str,
            'top': top,
            'scores': 0,
            'forms': 0,
            'lang': 'ru',
            'token': token
        })
        str = ''

        if result['code'] == 0:

            response = result['response']
            for item in response:
                for value in response[item]['vector']:
                    str += value + '\n'
        else:
            print('Ошибка при выполнении запроса:', result['msg'])
        return str
    else:
        print('Неверные имя пользователя или пароль')

