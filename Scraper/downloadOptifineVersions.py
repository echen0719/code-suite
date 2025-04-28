import requests
from getOptifineVersions import *

recommended, alternatives, previews = getOptifineVersions()
total = recommended + alternatives + previews

for i in range(0, len(total)):
    link = r'https://optifine.net/download?f={}'.format(total[i])
    request = requests.get(link)
    if request.status_code == 200:
        with open(total[i], 'wb') as file:
            file.write(request.content)
    else:
        print('Failed to download file. Status code: {}'.format(request.status_code))
        print(total[i])
        break