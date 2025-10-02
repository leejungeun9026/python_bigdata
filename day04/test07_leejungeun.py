import requests
from bs4 import BeautifulSoup
import pandas as pd

# 페이지 카운트 구하기
get_page_url = 'https://library.busan.go.kr/portal/module/libraryInfo/index.do?menu_idx=73&lib_cate_code=0001'
get_page_req = requests.get(get_page_url)
soup = BeautifulSoup(get_page_req.text, 'html.parser')
page_count = len(soup.select('#board_paging > span > a'))

# 함수 생성
def busan_librarys(datas) :
  # 페이지 만큼 반복
  for page in range(1, page_count + 1) :
    url = 'https://library.busan.go.kr/portal/module/libraryInfo/index.do?search_type=LIB_NAME&menu_idx=73&lib_cate_code=0001&viewPage=%d' %page
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')
    table_tr = soup.select('table.tbl-type01 > tbody > tr')

    for list in table_tr :
      loc = list.select_one('td:nth-child(1)').text.strip()
      name = list.select_one('th').text
      addr = list.select_one('td:nth-child(3)').text
      tel = list.select_one('td:nth-child(4)').text
      datas.append([loc, name, addr, tel])


# 함수 호출로 리스트 생성
datas = []
busan_librarys(datas)
print(datas)


# 파일 내보내기
df = pd.DataFrame(datas, columns=('지역', '도서관명', '주소', '전화번호'))
df.to_csv('day04\\busan_lib.csv', mode='w', encoding='utf-8-sig', index=False)