import requests
from bs4 import BeautifulSoup
url = "https://news.naver.com/main/list.nhn?mode=LPOD&mid=sec&oid=032"
req = requests.get(url)
html = req.text
soup = BeautifulSoup(html, 'html.parser')
list_ = soup.find_all("dl")

