import requests
from bs4 import BeautifulSoup

url = 'http://finance.naver.com/marketindex/'
req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')

rst = []
li = soup.select('#exchangeList > li')
for i in li :
  name = i.select_one('.h_lst > .blind').text
  price = i.select_one('.head_info > .value').text
  change = i.select_one('.head_info > .change').text
  blind = i.select_one('.head_info > .blind').text
  rst.append([name, price, change, blind])

print(rst)
