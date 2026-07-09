import requests
from bs4 import BeautifulSoup
import tqdm


def get_content(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    req = requests.get(url=url, headers=headers, timeout=10)
    req.encoding = "utf-8"
    html = req.text
    bs = BeautifulSoup(html, "lxml")
    texts = bs.find("div", id="booktxt")
    return texts.text.strip()


server = "https://www.bequke.com"
url = "https://www.bequke.com/xiaoshuo/0/151/"
req = requests.get(url=url)
req.encoding = "utf-8"
html = req.text
bs = BeautifulSoup(html, "lxml")
chapter = bs.find("div", class_="all")
chapters = chapter.find_all("li")
for chapter in tqdm.tqdm(chapters):
    href = chapter.find("a")["href"]
    title = chapter.find("a")["title"]
    url = server + href
    content = get_content(url)
    file_name = title + ".txt"
    with open(r"E:\电子书" + "\\" + file_name, "a", encoding="utf-8") as f:
        f.write(title + "\n" + "\n")
        f.write(content + "\n")
