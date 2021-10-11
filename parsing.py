import requests, re
from bs4 import BeautifulSoup as BS

page = 1
allThings = ''

while page != 10:

    r = requests.get('https://citaty.info/man/konfucii?page=' + str(page))
    html = BS(r.content, 'html.parser')

    for el in html.select(".view-content"):
        text = el.select(".field-item")
        print(text[0].text)
        allThings = allThings + str(text[0].text) + "\n"

    page = page + 1

print(allThings)

f = open("konfuci.txt", 'w')
f.write(allThings)
