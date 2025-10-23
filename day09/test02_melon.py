from bs4 import BeautifulSoup
import requests
import pandas as pd

# 1. 순위, 제목, 가수, 앨범 정보를 리스트에 담아 출력하기
# 2. pandas를 이용하여 수집한 데이터를 melon.csv 파일로 저장하기

header = {'User-agent' : 'Mozilla/5.0'}
url = "https://www.melon.com/chart/index.htm"
req = requests.get(url, headers=header)
soup = BeautifulSoup(req.text, 'html.parser')

trs = soup.select('#tb_list table > tbody > tr')

datas = []
for tr in trs :
  ranking = tr.select_one('span.rank').text
  title = tr.select_one('div.rank01 > span > a').text
  singer_list = tr.select('div.rank02 > a')
  singers = []
  for singer in singer_list :
    singers.append(singer.text)
  singer = "/".join(singers)
  album = tr.select_one('div.rank03 > a').text
  datas.append([ranking, title, singer, album])

# 출력
print(datas)

# csv저장
df = pd.DataFrame(datas, columns=('순위', '제목', '가수', '앨범'))
df.to_csv('day09/melon.csv', mode='w', index=False, encoding='utf-8-sig')
