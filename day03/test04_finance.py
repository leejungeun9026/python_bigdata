import requests
from bs4 import BeautifulSoup

url1 = ('https://finance.naver.com/item/main.naver?code=252670')
url2 = ('https://finance.naver.com/item/main.naver?code=251340')
req1 = requests.get(url1)
req2 = requests.get(url2)

# 객체 생성
soup1 = BeautifulSoup(req1.text,'html.parser')
soup2 = BeautifulSoup(req2.text,'html.parser')

lst = []
req1_title = soup1.select_one('#middle > div.h_company > div.wrap_company > h2 > a').text
req1_today = soup1.select_one('div > p.no_today > .no_up > .blind').text
req1_list = [req1_title, req1_today]
lst.append(req1_list)

req2_title = soup2.select_one('#middle > div.h_company > div.wrap_company > h2 > a').text
req2_today = soup2.select_one('div > p.no_today > .no_up > .blind').text
req2_list = [req2_title, req2_today]
lst.append(req2_list)

print(lst)
