import random

def randomNumber(msg):
    try:
        number = [int(s) for s in msg.split() if s.isdigit()]
        if (number[0] < number[1]) and (len(number) == 2):
            return random.randint(number[0], number[1])
        return "Что-то не так"
    except:
        return "Wrong"
