from twilio.rest import Client
import requests
import time

# replace these with info from Twilio
Account_SID = ''
Auth_Token = ''
Sender_Num = ''
Reciever_Num = ''

def sendText(price):
    client = Client(sid, token)
    message = client.messages.create(body='Current price: {}'.format(price), from_=sender, to=reciever)

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
    if price <= 90000:
        sendText(price)
    print(price)
    time.sleep(5)
