import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
target = "https://www.bequke.com/book/0/151/274/"
req = requests.get(url=target, headers=headers)
req.encoding = "utf-8"
html = req.text
bs = BeautifulSoup(html, "lxml")
texts = bs.find("div", id="booktxt")
print(texts)
