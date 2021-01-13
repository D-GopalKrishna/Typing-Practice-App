from requests_html import HTMLSession
import requests
from bs4 import BeautifulSoup
import re




def removetags(x):
    return re.sub(re.compile('<.*?>'), '', x)


def remove_diff_quotation_mark(x):
    x = re.sub(r'“', '"', x)
    x = re.sub(r'”', '"', x)
    x = re.sub(r'’', "'", x)
    x = re.sub(r"\xa0", " ", x)

    return x



def web_text():
    req = requests.get('https://onezero.medium.com/burn-the-chambers-stop-the-steal-facebook-groups-erupt-amidst-capitol-building-siege-3844992f71f')
    # print(req.encoding)
    soup = BeautifulSoup(req.content, 'html.parser')

    # title1 = soup.find('title')
    # print(title1)
    # print("")

    # title2 = soup.find_all('title')
    # print(title2)
    # print("")

    contb = soup.find_all('p')

    # The code to clean it.
    superflash = []
    for i in contb:
        # print(type(i))
        i = str(i)
        # print(type(i))
        # print(i)

        i = removetags(i)
        i = remove_diff_quotation_mark(i)
        superflash.append(i)
        # print("")

    return (superflash, len(superflash))








# print(web_text())









