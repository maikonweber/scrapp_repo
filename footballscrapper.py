
import requests
from time import sleep
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd
from datetime import datetime


# conn = psycopg2.connect(database="cook", user="cook", password="cook", port='5732')

headers = {
    'Host': 'e-com.secure.force.com',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64)',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch',
}


response = requests.get('https://www.receiteria.com.br/receitas-fit/', headers)
soup = BeautifulSoup(response.content, 'html.parser')

receitas = soup.find_all('div', attrs={'class': 'receita'})
array = []
for y in receitas:

    a = y.find('a', attrs={'class': 'imglink'})
    title = y.find('div', attrs={'class': 'recipe-head'})
    text = y.find('div', attrs={'class': 'info'})

    dict = {
        'titulo': title.text.split(' '),
        'href': a['href'],
        'resume': text.text,
        'ingredientes': '',
        'preparo': ''
    }
    array.append(dict)

for y in array:
    y['href']
    response = requests.get(y['href'])
    soup = BeautifulSoup(response.content, 'html.parser')
    ingredientes = soup.find('div', attrs={'class': 'ingredientes mt-4 mb-4'})
    preparo = soup.find('div', attrs={'class': 'preparo mt-4 mb-4'})
    y['ingredientes'] = ingredientes.text
    y['preparo'] = preparo.text

    # y['preparo'] = preparo.text
    # divimg = soup.find('div', attrs={'class': 'superimg'})
    # img = divimg.find('img')

for y in array:

    sleep(1)
    print(y['preparo'])
    # request.post()
    x = requests.post('http://localhost:3055/api/cook-book', json=y)
    print(x.text)
