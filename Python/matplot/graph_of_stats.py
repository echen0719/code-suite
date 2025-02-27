import matplotlib.pyplot as plt # remember to ask people to install matplotlib
import csv
from datetime import datetime
import os

# I got this off the web so I don't really know what this is (some plz explain)
os.chdir(os.path.dirname(os.path.abspath(__file__))) # in case Python runs in system32 folder instead

dates, kills_elo, kd_ratio = [], [], [] # makes empty list for csv file to append to

with open('stats.csv') as file:
    reader = csv.DictReader(file) # reads csv
    for row in reader:
        dates.append(datetime.strptime(row['Date'], '%m/%d/%Y')) # adds dates in format to list
        kills_elo.append(float(row['Kills Elo'])) # adds kills_elo to list
        kd_ratio.append(float(row['KD'])) # adds kd_ratio to list

# I think white background looks good, could be changed to dark.

fig, ax1 = plt.subplots()
ax1.set_xlabel('Date') # sets x-axis label
ax1.set_ylabel('Kills Elo', color='tab:blue') # sets y-axis label
ax1.plot(dates, kills_elo, color='tab:blue') # plots kills_elo as points
ax1.tick_params(axis='y', labelcolor='tab:blue') # sets color of kills_elo line

ax2 = ax1.twinx() # copies axis 1 (dates)
ax2.set_ylabel('K/D Ratio', color='tab:green') # sets y-axis label
ax2.plot(dates, kd_ratio, color='tab:green', label='KD') # plots kd_ratio as points
ax2.tick_params(axis='y', labelcolor='tab:green') # sets color of kd_ratio line

plt.title('Kills Elo and K/D Ratio Over Time')
plt.tight_layout()
plt.show()

# I used matplotlib's documentation and Stack Overflow to create a graph of the data from the csv file.