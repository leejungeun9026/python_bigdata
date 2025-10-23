# https://www.hanatour.com/mma/smn/EX00000020

# 제주도 > 호텔 검색 후
# 호텔이름, 별점, 가격 
# 1.파일로 내보기 ==> hanatour.csv
# 2.별점 에 대한 그래프  ==> 막대그래프
# 3.db 테이블 추가하기

# 4. 테이블에서 별점을 select해서 별점 별 파이그래프 그리기
# (4점대 ~~%, 5점대 ~~~%)
###################
# 파이그래프 그리기

import pymysql
import matplotlib.pyplot as plt
import matplotlib as mpl
con = pymysql.connect(host='127.0.0.1', user='root', password='1234',
                      database='pythondb', charset='utf8')


cur = con.cursor()
select_sql = "select floor(stars), count(*) from hanatour_table group by floor(stars)"
cur.execute(select_sql)
result = cur.fetchall()

x =[]
y =[]

for row in result:
  x.append(str(row[0])+' 점대')
  y.append(row[1])

con.close()

font_name = mpl.font_manager.FontProperties(
    fname='c:/Windows/fonts/malgun.ttf').get_name()
mpl.rc('font', family=font_name)

#파이그래프
plt.pie(y, labels=x,autopct='%.1f%%')
plt.show()

