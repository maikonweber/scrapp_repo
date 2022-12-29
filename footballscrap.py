import requests
from time import sleep
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd
from datetime import datetime


headers = {
    'Host': 'e-com.secure.force.com',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64)',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch',
}


response = requests.get('https://www.livesport.com/br/futebol/brasil/campeonato-paulista/#/zyFj2OVF/table/overall', headers)
soup = BeautifulSoup(response.content, 'html.parser')
table = soup.find_all('a')
print(table)

# for y in a:
#   print(y.text)