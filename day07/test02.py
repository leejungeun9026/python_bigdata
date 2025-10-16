import matplotlib.pyplot as plt
import matplotlib as mpl
import pymysql

# 1. db에서 점수 가져오기
con = pymysql.connect(host='127.0.0.1', user='leejungeun', password='1234', database='pythondb', charset='utf8')

cur = con.cursor()

sql = '''select
          case
            when stars = 5 then '5점대'
            when stars between 4 and 5 then '4점대'
            when stars between 3 and 4 then '3점대'
            when stars between 2 and 3 then '2점대'
            when stars between 1 and 2 then '1점대'
            end as star,
            count(*) as count
        from pythondb.hanatour_table
        group by star;'''

cur.execute(sql)
result = cur.fetchall()
cur.close()

# 파이 그래프
x = [i[0] for i in result]
y = [i[1] for i in result]

# 폰트 설정
font_name = mpl.font_manager.FontProperties(fname='c:/Windows/fonts/malgun.ttf').get_name()
mpl.rc('font', family=font_name)

plt.pie(y, labels=x, autopct='%.1f%%')
plt.title('점수대별 호텔 비율', fontsize=14)
plt.show()