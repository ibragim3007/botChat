import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from config import token
from createRadnomJokes import GetRandomC, GetRandomTur, GetRandomPapich, getRandomConfuci
from getSinonims import activeateFindSyns
from vector import activeateFindVectors
from randomNumber import randomNumber
import random

vk_session = vk_api.VkApi(token=token)
longpoll = VkBotLongPoll(vk_session, 207785586)


def sender(id, text):
    vk_session.method('messages.send', {'chat_id': id, 'message': text, 'random_id': 0})


for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        if event.from_chat:
            id = event.chat_id
            msg = event.object.message['text'].lower()
            print(event.object.message)
            idFromWho = event.object.message['from_id']

            if msg in ['дай цитату', 'цитату', 'цитата заратустры']:
                sender(id, GetRandomC())

            if msg in ['про тюрьму', 'тюремная цитата','тюремную цитату' , 'цитата про тюрьму','цитату про тюрьму']:
                sender(id, GetRandomTur())

            if msg in ['папич', 'папич скажи', 'цитата папича', 'цитату папича']:
                sender(id, GetRandomPapich())

            if msg in ['я никита бердник', 'я вадим сергеев', 'я фанат влада а4']:
                sender(id, 'тo есть долбаеб?')

            if msg in ['я тимикс', 'я timix', 'тимикс', 'timix']:
                sender(id, "URARARAR")

            if msg.startswith('сколько'):
                if msg in ['сколько iq у ибрагима', 'iq ибрагима', 'сколько айкью у ибрагима', 'айкью ибрагима',
                           'iq у ибрагима сколько']:
                    sender(id, str(random.randint(120, 250)))
                else:
                    sender(id, str(random.randint(20, 100)))

            if msg.startswith('рандомное число'):
                sender(id, randomNumber(msg))

            if msg in ['конфуций']:
                sender(id, getRandomConfuci())

            if msg in ['хип']:
                sender(id, 'хоп')

            if msg.startswith('синоним'):
                sender(id, activeateFindSyns(msg))

            if msg.startswith('вектор'):
                sender(id, activeateFindVectors(msg))

            if idFromWho == 236161348:
                sender(id, 'долбаеб хватит писать')

