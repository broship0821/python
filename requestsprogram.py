import requests
from bs4 import BeautifulSoup
URL = "https://search.naver.com/search.naver?&where=news&query=%EC%BD%94%EB%A1%9C%EB%82%98&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so:r,p:all,a:all&mynews=0&cluster_rank=71&start=1&refresh_start=0"
req = requests.get(URL)
html = req.text
soup = BeautifulSoup(html, 'html.parser')
list_ = soup.find("ul", class_="type01")
# 제목 가져오기
texts = list_.find_all("dt")
for text in texts:
    # print(text.find("a", class_="_sp_each_title"))
    print(text.a["title"])
# 링크 가져오기
links = list_.find_all("dd", class_="txt_inline")
# url = links.find("a", class_="_sp_each_url")
url = links.a["href"]
print(links)
# 링크 가져오기 실패 계속 연구하기