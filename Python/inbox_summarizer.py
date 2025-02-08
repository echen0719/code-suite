import email
import imaplib
from datetime import datetime

mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login("", "") # email, imap password

mail.select('inbox')

date = datetime.today().strftime("%d-%b-%Y") # Day-Month-Year
messages = mail.search(None, "ALL") # trying to get today's emails

ids = []

for block in messages:
    ids += block.split() # i don't understand this part

for i in ids:
    data = mail.fetch(i, "(RFC822)")

    for response in data:
        if isinstance(response, tuple):
            msg = email.message_from_bytes(response[1])
            print("From:", msg["From"])
            print("Subject:", msg["Subject"])

            if msg.is_multipart(): # need to look at docs
                for part in msg.walk():
                    if part.get_content_type() == "text/plain":
                        print("Body:", part.get_payload(decode=True).decode())
            else:
                print("Body:", msg.get_payload(decode=True).decode())

# https://humberto.io/blog/sending-and-receiving-emails-with-python/
