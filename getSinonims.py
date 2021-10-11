import requests
from config import token_Paraphaser
import json
from urllib.request import urlopen
from urllib.parse import urlencode, quote_plus

def getSinonim(query, top):

    payload = {'c': 'syns',
               'query': query,
               'top': top,
               'scores': 0,
               'forms': 0,
               'format': 'json',
               'lang': 'ru',
               'token': token_Paraphaser}

    r = requests.post('http://paraphraser.ru/api/', data=payload)

    result = r.json()

    text = ''

    if result['code'] == 0:
        response = result['response']

        for item in response:
            for value in response[item]['syns']:
                text += value + "\n"

    return text

def activeateFindSyns(str):
    str = str[0:89]
    return getSinonim(str.partition(' ')[2], 5)

print(activeateFindSyns("синоним машина"))

# def send(payload):
#     params = urlencode(payload, quote_via=quote_plus)
#     url = 'http://paraphraser.ru/api?{0}'.format(params)
#     try:
#         return json.loads(urlopen(url).read().decode('utf-8'))
#     except Exception as err:
#         return json.loads(err.read().decode('utf-8'))
#
#
# token = token_Paraphaser
#
# if token is not None:
#
#     result = send({
#         'c': 'vector',
#         'query': 'кот ест рыбку',
#         'top': 4,
#         'scores': 0,
#         'forms': 0,
#         'lang': 'ru',
#         'token': token
#     })
#
#     if result['code'] == 0:
#
#         response = result['response']
#         for item in response:
#             for value in response[item]['vector']:
#                 print(value)
#     else:
#         print('Ошибка при выполнении запроса:', result['msg'])
# else:
#     print('Неверные имя пользователя или пароль')