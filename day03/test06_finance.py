import requests
from bs4 import BeautifulSoup

url = 'http://finance.naver.com/marketindex/'
req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')

#exchangeList > li.on > a.head.usd > div
txt = soup.select_one('#exchangeList > li.on > a.head.usd > div')
print(txt)
print(txt.select('span')[0].text)
print(txt.select('span')[3].string)
print(txt.select('span')[4].string)

print('-'*20)
#exchangeList > li.on > a.head.usd > div > span.value
value = soup.select_one('#exchangeList > li.on > a.head.usd > div > span.value').text
print(value)

# //*[@id="exchangeList"]/li[1]/a[1]