import requests
from bs4 import BeautifulSoup

target = 'https://www.bequke.com/book/0/151/274/'
req = requests.get(url = target)
req.encoding = 'utf-8'
html = req.text
bs = BeautifulSoup(html, 'lxml')
texts = bs.find('div',id='booktxt')
print(texts.text.strip())