import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.aladin.co.kr/shop/common/wbest.aspx?BranchType=1&BestType=Bestseller'
req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')

books = soup.select('div.ss_book_box')

book_lst = []
for book in books :  
  li = book.select('.ss_book_list:nth-child(1) > ul > li')
  title = book.select_one('.bo3').text
  author = li[-3].select_one('a').text
  price = li[-2].select_one('.ss_p2 > em').text
  book_lst.append([title, author, price])

book_tbl = pd.DataFrame(book_lst, columns=('책 제목', '저자', '가격'))
book_tbl.to_csv('day04\\books.csv', mode='w', encoding='utf-8-sig', index=False)