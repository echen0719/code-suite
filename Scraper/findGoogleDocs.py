import requests
from bs4 import BeautifulSoup
import random

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890-_'

def getRandomDocsLink():
    rndString = ''
    for _ in range(44):
        randInt = random.randint(0, 63)
        rndString += letters[randInt]
    return 'https://docs.google.com/document/d/' + rndString

count = 1
while True:
    link = getRandomDocsLink()
    try:
        request = requests.get(link, timeout=3)
        if request.status_code == 200:
            print(link)
            break
    except:
        continue
    print('Current: #' + str(count))
    count += 1
