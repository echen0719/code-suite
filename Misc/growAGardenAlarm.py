import time
import requests
import os
from playsound import playsound
from datetime import datetime, timezone

# write to dingdingdingalarm.mp3 in home
loc = os.path.join(os.path.expanduser("~"), "dingdingdingalarm.mp3")
request = requests.get('https://cdn.pixabay.com/download/audio/2022/03/24/audio_4ff823c44c.mp3?filename=ding-101492.mp3')
# some random mp3 'ding' file I found

if request.status_code == 200:
    with open(loc, 'wb') as file:
        file.write(request.content)
else:
    print("Try Again. Something wrong. Status Code: {}".format(request.status_code))
    exit()

while True:
    now = datetime.now(timezone.utc)
    
    # 5th minute of every hour
    if now.minute % 5 == 0 and now.second == 0:
        playsound(loc)
        time.sleep(60) # each minute
    else:
        time.sleep(1) # so cpu doesn't lag
