import requests
from time import sleep
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd
from datetime import datetime

url = 'https://guia.melhoresdestinos.com.br/#destinos-nacionais'

headers = {
    'Host': 'e-com.secure.force.com',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64)',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch',
}
response = requests.get(url, headers)

soup = BeautifulSoup(response.content, 'html.parser')

divs = soup.find_all('div', attrs={'class': 'destino-card'})
print(divs)

href = []
for y in divs:
  hrefx = y.find('a')
  dict = {
   'place' : y.text,
   'href' : hrefx['href'],
   'principal' : '', 
   'another' : []
  }

  href.append(dict)

for x in href:
  url = 'https://guia.melhoresdestinos.com.br' + x['href']
  response = requests.get(url, headers)
  soup = BeautifulSoup(response.content, 'html.parser')
  p = soup.find('div', attrs={'class' : 'post-body'})
  x['principal'] = p.text
  a = soup.find_all('a', attrs={'class' : 'icon-viagem'})
  for o in a:
    print(o['href'])
    dict = {
      'href' : o['href'],
      'text' : ''
    }
    url = 'https://guia.melhoresdestinos.com.br' + x['href']
    response = requests.get(url, headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    p = soup.find('div', attrs={'class' : 'post-body'})
    dict['text'] = p.text
    x['another'].append(dict)  
  p = requests.post('http://localhost:3055/api/travel', json=x)
  print(p)
