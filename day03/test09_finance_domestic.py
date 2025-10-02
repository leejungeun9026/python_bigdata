import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/sise/'
req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')
ul = soup.select_one('#popularItemList')
print(ul)
li = soup.select('#popularItemList > li')

data = []
for i in li :
  title = i.select_one('a').text
  price = i.select_one('span').text
  updown = i.select_one('span.blind').text
  data.append([title, price, updown])
print(data)
