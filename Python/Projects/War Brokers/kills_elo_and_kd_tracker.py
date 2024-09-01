import requests
import re
import csv
from datetime import datetime
import os

# I got this off the web so I don't really know what this is (some plz explain)
os.chdir(os.path.dirname(os.path.abspath(__file__))) # in case Python runs in system32 folder instead

# reads UID from uid.txt and sets 'uid' variable.
with open('uid.txt', 'r') as uid_file:
    uid = uid_file.read().strip() # reads the file and removes the whitespaces

# fetches player kills and deaths using uid
wb_stats = f"https://stats.warbrokers.io/players/i/{uid}"
request = requests.get(wb_stats) # HTTP GET request

if request.status_code == 200: # if GET request was successful (200)
    contents = request.text # assigns HTTP repsonse to 'contents' variable
else:
    print(f"Try Again. Something wrong. Status Code: {request.status_code}") # failed
    exit()

# extract text within a div called 'player-details-number-box-value'
divClass = r'<div\s+class="player-details-number-box-value">\s*([\d,]+)\s*</div>'
foundDiv = re.findall(divClass, contents)

kills = foundDiv[1].replace(',', '') # 2nd div match
deaths = foundDiv[2].replace(',', '') # 3rd div match
kd = round(float(kills) / float(deaths), 2) # calculates KD and rounds to hundreths

# fetches player kills elo using uid
pomps_api = f"https://wbapi.wbpjs.com/players/getPlayer?uid={uid}" # thank you developomp
request = requests.get(pomps_api) # HTTP GET request

if request.status_code == 200: # if GET request was successful (200)
  data = request.json() # parses JSON

kills_elo = data.get("killsELO") # gets kills elo from JSON

# writes all data to stats.csv
date = datetime.today().strftime('%m/%d/%Y') # format of time
filename = 'stats.csv'

if not os.path.exists(filename) or os.stat(filename).st_size == 0: # checks if file exists and is empty
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Date', 'Kills Elo', 'KD']) # makes rows for the csv file and writes

with open(filename, mode='a', newline='') as file: 
    writer = csv.writer(file)
    writer.writerow([date, kills_elo, kd]) # writes data to csv file

print("Complete! File saved to stats.csv.") # compiler output