import pymysql
import matplotlib.pyplot as plt
import matplotlib as mpl

# csv읽어와서 테이블 생성
# 생성한 테이블에 데이터 넣기

# 파일 가져오기
with open('day06\\naver_movie.csv', 'r', encoding='utf-8-sig') as inFp:
  naver_movie = []
  next(inFp)  # 첫 번째 줄(헤더) 건너뛰기
  for data in inFp :
    row = data.strip()
    row_list = row.split(',')
    naver_movie.append(row_list)

# DB연결
con = pymysql.connect(host="127.0.0.1", user="leejungeun", password="1234", database="pythondb", charset="utf8")

# 커서 생성
cur = con.cursor()

# 테이블 삭제 및 생성
cur.execute('drop table if exists movie_table')
cur.execute('create table movie_table(ranking int, title varchar(45), stars float, views int)')

# insert 쿼리 생성
insert_sql = "insert into movie_table(ranking, title, stars, views) values(%s, %s, %s, %s)"

# insert 쿼리 실행
for row in naver_movie :
  ranking = row[0]
  title = row[1]
  stars = row[2]
  views = row[3]
  cur.execute(insert_sql, (ranking, title, stars, views))
con.commit()


# 그래프를 위한 x, y축 데이터 넣기
cur.execute("select * from movie_table")
result = cur.fetchall()
x = []
y = []
for row in result :
  x.append(row[1])
  y.append(row[3]/10000)

# DB 자원 해제
con.close()

# 폰트 설정
font_name = mpl.font_manager.FontProperties(fname='c:/Windows/fonts/malgun.ttf').get_name()
mpl.rc('font', family=font_name)

# 막대그래프
plt.bar(x, y)
plt.title('누적 관객수(만명)')
plt.xlabel('영화 제목')
plt.ylabel('누적 관객 수(만명)')
plt.show()

# 파이그래프
plt.pie(y, labels=x, autopct='%.1f%%')
plt.show()