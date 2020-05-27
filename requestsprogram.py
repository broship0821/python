import requests
from bs4 import BeautifulSoup
URL = "https://search.naver.com/search.naver?&where=news&query=%EC%BD%94%EB%A1%9C%EB%82%98&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so:r,p:all,a:all&mynews=0&cluster_rank=71&start=1&refresh_start=0"
req = requests.get(URL)
html = req.text
soup = BeautifulSoup(html, 'html.parser')
list_ = soup.find("ul", class_="type01")
# # 제목 가져오기
# texts = list_.find_all("dt")
# for text in texts:
#     # title = text.find("a", class_="_sp_each_title")
#     title = text.a["title"]
# print(title)
# 제목 가져오기 - 리스트로 묶어서 해보기
texts = list_.find_all("dt")
text_list = [texts]
print(text_list)
# for text in text_list:
#     # title = text.find("a", class_="_sp_each_title")
#     title = text.a["title"]
# print(title)



# 링크 가져오기
links = list_.find_all("dd", class_="txt_inline")
for link in links:
    url = link.a["href"]
print(url)

#맨 마지막꺼만 출력됨