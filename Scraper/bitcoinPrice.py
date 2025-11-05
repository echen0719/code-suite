import requests
import time

def sendText():

def getPrice():
    request = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd')
    
    if request.status_code == 200:
        data = request.json()
        price = data['bitcoin']['usd']
        return price
    
    else:
        print("Try Again. Something wrong. Status Code: {}".format(request.status_code))
        exit()

while True:
    price = getPrice()
    # if price <= 90000:
        # send text
    print(price)
    time.sleep(5)
