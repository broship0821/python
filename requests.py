import requests
URL = "https://news.naver.com/main/list.nhn?mode=LPOD&mid=sec&oid=022"
a = requests.get(URL)
print(a)
# requests 설치 실패, 설치 방법 알기