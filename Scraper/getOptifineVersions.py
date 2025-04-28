import requests
from bs4 import BeautifulSoup
import re

request = requests.get('https://optifine.net/downloads')

def getOptifineVersions():
    if request.status_code == 200:
            html = request.content
    else:
        print('Failed to download file. Status code: {}'.format(request.status_code))

    soup = BeautifulSoup(html, 'html.parser')

    # updated when each MC version comes out so it can be hard-coded
    
    recommended = [
        'OptiFine_1.21.4_HD_U_J3.jar', 'OptiFine_1.21.3_HD_U_J2.jar', 'OptiFine_1.21.1_HD_U_J1.jar', 
        'OptiFine_1.20.4_HD_U_I7.jar', 'OptiFine_1.20.1_HD_U_I6.jar', 'OptiFine_1.19.4_HD_U_I4.jar', 
        'OptiFine_1.19.3_HD_U_I3.jar', 'OptiFine_1.19.2_HD_U_I2.jar', 'OptiFine_1.19.1_HD_U_H9.jar', 
        'OptiFine_1.19_HD_U_H9.jar', 'OptiFine_1.18.2_HD_U_H9.jar', 'OptiFine_1.18.1_HD_U_H6.jar', 
        'OptiFine_1.18_HD_U_H3.jar', 'OptiFine_1.17.1_HD_U_H1.jar', 'OptiFine_1.16.5_HD_U_G8.jar', 
        'OptiFine_1.16.4_HD_U_G7.jar', 'OptiFine_1.16.3_HD_U_G5.jar', 'OptiFine_1.16.2_HD_U_G5.jar', 
        'OptiFine_1.16.1_HD_U_G2.jar', 'OptiFine_1.15.2_HD_U_G6.jar', 'OptiFine_1.14.4_HD_U_G5.jar', 
        'OptiFine_1.14.3_HD_U_F2.jar', 'OptiFine_1.14.2_HD_U_F1.jar', 'OptiFine_1.13.2_HD_U_G5.jar', 
        'OptiFine_1.13.1_HD_U_E4.jar', 'OptiFine_1.13_HD_U_E4.jar', 'OptiFine_1.12.2_HD_U_G5.jar', 
        'OptiFine_1.12.1_HD_U_G5.jar', 'OptiFine_1.12_HD_U_G5.jar', 'OptiFine_1.11.2_HD_U_G5.jar', 
        'OptiFine_1.11_HD_U_G5.jar', 'OptiFine_1.10.2_HD_U_I5.jar', 'OptiFine_1.10_HD_U_I5.jar', 
        'OptiFine_1.9.4_HD_U_I5.jar', 'OptiFine_1.9.2_HD_U_E3.jar', 'OptiFine_1.9.0_HD_U_I5.jar', 
        'OptiFine_1.8.9_HD_U_M5.jar', 'OptiFine_1.8.8_HD_U_I7.jar', 'OptiFine_1.8.0_HD_U_I7.jar', 
        'OptiFine_1.7.10_HD_U_E7.jar', 'OptiFine_1.7.2_HD_U_F7.jar']

    allVersions = [] # temporary list variable
    alternatives = []
    previews = []

    # link is inside an anchor element inside a table data set
    for td in soup.find_all('td', {'class': 'colMirror'}):
        anchor = td.find('a')
        if anchor:
            # this regex will get XXXXX.jar from the href tag in the anchor element
            link = re.search(r"([A-Za-z0-9_\.]+\.jar)", anchor.get('href'))
        if link:
            allVersions.append(link.group())

    for version in allVersions:
        if 'preview' in version:
            previews.append(version)
        elif version not in recommended:
            alternatives.append(version)

    return recommended, alternatives, previews

# just learned that this is the right way to test
if __name__ == '__main__':
    recommended, alternatives, previews = getOptifineVersions()
    print('recommended = ', recommended)
    print('alternatives = ', alternatives)
    print('previews = ', previews)
    print(str(len(recommended)) + ', ' + str(len(alternatives)) + ', ' + str(len(previews)))
