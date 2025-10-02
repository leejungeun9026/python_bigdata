import requests
from bs4 import BeautifulSoup

url = "https://entertain.daum.net/ranking/keyword"
req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')

keyword_list = soup.select(".list_topkey > li")

datas = []
for k in keyword_list :
  keyword = k.select_one(".txt_g").text
  datas.append(keyword)
print(datas)