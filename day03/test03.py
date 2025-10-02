import requests
from bs4 import BeautifulSoup

# req = requests.get('https://finance.naver.com/item/main.naver?code=252670')
# print(req.content)

url = ('https://finance.naver.com/item/main.naver?code=252670')
req = requests.get(url)

# 객체 생성
soup = BeautifulSoup(req.text,'html.parser')
# print(soup)


print(soup.select_one('#middle > div.h_company > div.wrap_company > h2 > a').text)

today = soup.select_one('div > p.no_today')
print(today)
today_value = today.select_one('.no_up > .blind')
print(today_value.text)