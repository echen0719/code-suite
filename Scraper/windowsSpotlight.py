import requests
from bs4 import BeautifulSoup

pageNum = 0

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
request = requests.get('https://windows10spotlight.com/', headers=headers)

if request.status_code == 200:
    soup = BeautifulSoup(request.text, 'html.parser')
    pageNums = []
    for pageNum in soup.find_all('a', {'class': 'page-numbers'}):
        pageNums.append(pageNum.get_text(strip=True))
    pageNum = int(pageNums[2].replace(',', ''))

else:
    print(f"Try Again. Something wrong. Status Code: {request.status_code}") # failed
    exit()

for i in range(0, pageNum + 1):
    request = requests.get('https://windows10spotlight.com/page/{}'.format(i), headers=headers)
    if request.status_code == 200:
        soup = BeautifulSoup(request.text, 'html.parser')
        imgs = []
        for img in soup.find_all('img', {'class': 'thumbnail wp-post-image'}):
            imgs.append(img.get('src'))
        print(imgs)

    else:
        print(f"Try Again. Something wrong. Status Code: {request.status_code}") # failed
        exit()