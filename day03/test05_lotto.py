import requests
from bs4 import BeautifulSoup

url = 'https://m.dhlottery.co.kr/gameResult.do?method=byWin'
req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')

lottonum = soup.select('#container > div > div.bx_lotto_winnum > .ball')

rst = []
for i in lottonum :
  rst.append(i.text)
print(rst)