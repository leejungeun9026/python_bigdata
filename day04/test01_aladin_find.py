import requests
from bs4 import BeautifulSoup

url = 'https://www.aladin.co.kr/shop/wbrowse.aspx?CID=351'
req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')

###### find로 바꿔보기
# item = soup.select_one('ul.b-booklist')
item2 = soup.find('ul',{'class' : 'b-booklist'})
# all_text = item.select('div.b-text')
all_text2 = item2.findAll('div',{'class': 'b-text'})


result = []
for i in all_text2 :
  # title = i.select_one('h4 > a').text
  title = i.find('a').text

  # author = i.select_one('div.b-author').text
  author = i.find('div', {'class' : 'b-author'}).text
  
  # price = i.select_one('div.b-price > strong').text
  price_class = i.find('div', {'class' : 'b-price'})
  price = price_class.find('strong').text
  
  result.append([title, author, price])

print(result)