import requests, re
from bs4 import BeautifulSoup as BS
import random


def UpdateC():
    page = 1
    allThings = ''

    while page != 10:

        r = requests.get('https://citaty.info/character/zaratustra?page='+str(page))
        html = BS(r.content, 'html.parser')

        for el in html.select(".view-content > .quotes-row"):
            text = el.select("p")
            allThings = allThings + str(text[0].text) + "\n"

        page = page + 1


    print(allThings)

    f = open("zaratustra.txt", 'w')
    f.write(allThings)

def fileRandomLine(path):
    f = open(path, 'r')
    s = []

    for line in f:
        s.append(line)

    return s[random.randint(0, len(s))]

def GetRandomC():
    return fileRandomLine("turima.txt")

def GetRandomTur():
    return fileRandomLine("zaratustra.txt")

def GetRandomPapich():
    return fileRandomLine("papich.txt")

def getRandomConfuci():
    return fileRandomLine("konfuci.txt")