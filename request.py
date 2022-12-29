import requests
from time import sleep
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd
from datetime import datetime

array = []

url = ['https://br.tradingview.com/news/',
       'https://br.tradingview.com/news/?market=crypto',
       'https://br.tradingview.com/news/?market=economic']

for y in url:

    headers = {
        'Host': 'e-com.secure.force.com',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64)',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
    }
    response = requests.get(y, headers)

    soup = BeautifulSoup(response.content, 'html.parser')
    # div = soup.find('div', attrs={'class' : 'grid-IELnCmNm'})
    divs = soup.find_all(
        'a', attrs={'class': 'card-gaCYEutU cardLink-gaCYEutU'})
    # print(divs)
    for y in divs:
        y['href']
        y.find('relative-time').text
        y.find('span', attrs={'class': 'title-C9RvkKmg'})
        dict = {
            'href': y['href'],
            'relative-time': y.find('relative-time').text,
            'resume': y.find('span', attrs={'class': 'title-C9RvkKmg'}).text,
            'conteudo': ''
        }
        array.append(dict)

print(array)
for x in array:
    url = 'https://br.tradingview.com' + x['href']
    print(url)
    response = requests.get(url, headers)
    print(response)
    soup = BeautifulSoup(response.content, 'html.parser')
    p = soup.find_all('p')
    array = []
    for i in p:
        array.append(i.text)
    print(array)
    x['conteudo'] = ''.join(array)
    print(x)
    #     print(y.previous_sibling)
    #     x = y.find('span')
    #     l = y.find('div')

    #     split = y.text.split(' ')
    #     rescontent = l.text.replace('anteontem', '')
    #     cleartext = rescontent.replace('Reuters', '')
    #     fonte = x.find('span')

    #     href = y.next_siblings
    #     # print(href)
    #     print(href)
    #     dict = {
    #         'date': x.text.replace('Reuters', ''),
    #         'fontpe': fonte.text,
    #         'content': cleartext,
    #         'href': ''
    #         }

    #     # ReutersEstoques
    #     if (dict["date"] == 'anteontem'):
    #         date = datetime.now()
    #         tz = datetime.timestamp(date) - 2 * 24*60*60
    #         dict['date'] = datetime.timestamp(date)

    #         # print()

    #         # split = y.text.split(' ')
    #         # if (split[0] == 'há'):
    #         #     print(split[0], split[1], split[2], split[2].split('Reuters'))
    #         #     print(split[0])
