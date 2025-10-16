import pymysql
import matplotlib.pyplot as plt
import matplotlib as mpl

# 전역변수 선언
inStr = '''죽는 날까지 하늘을 우러러 한 점 부끄럼이 없기를,
잎새에 이는 바람에도 나는 괴로워했다.
별을 노래하는 마음으로 모든 죽어가는 것을 사랑해야지.
그리고 나한테 주어진 길을 걸어가야겠다.
오늘 밤에도 별이 바람에 스치운다. '''

# DB연결
con = pymysql.connect(host="127.0.0.1", user="leejungeun", password="1234", database="pythondb", charset="utf8")

# 커서 객체 생성
cur = con.cursor()

# 커서를 통해 쿼리 실행
cur.execute('drop table if exists countTable') # 테이블이 있으면 삭제하기
cur.execute('create table countTable(onechar varchar(10), count int)')  # 문자, 숫자 넣기

for ch in inStr:
  if 'ㄱ' <= ch <= '힣' :
    cur.execute("select * from countTable where onechar = '" + ch + "'")
    row = cur.fetchone()
    if row == None :
      # 테이블에 문자가 없는 경우 -> insert
      cur.execute("insert into counttable values('" + ch + "', " + str(1) + ")")
    else : 
      # 테이블에 문자가 있는 경우 -> update
      cnt = row[1]
      cur.execute("update counttable set count = " + str(cnt + 1) + 
                  " where onechar = '" + ch + "'")

con.commit()

# 결과 조회
cur.execute("select * from counttable order by count desc")
print('원문\n', inStr)
print('='*20)
print('문자\t 빈도수')
print('='*20)

while(True) :
  row = cur.fetchone()
  if row == None :
    break
  ch = row[0]
  cnt = row[1]
  print("%4s %5d" %(ch, cnt))



# count 개수를 막대그래프로 표시
count_sql = "select count, count(*) from counttable group by count"
cur.execute(count_sql)
result = cur.fetchall()

x = []
y = []
for row in result :
  x.append(row[0])
  y.append(row[1])

con.close()


# 폰트 설정
font_name = mpl.font_manager.FontProperties(fname='c:/Windows/fonts/malgun.ttf').get_name()
mpl.rc('font', family=font_name)

# 막대그래프
plt.bar(x, y)
plt.title('음절 빈도수')
plt.xlabel('음절')
plt.ylabel('개수')
plt.show()


# 파이그래프
plt.pie(y, labels=x, autopct='%.1f%%')
plt.show()


