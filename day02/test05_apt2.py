import re
import csv

# apt_201910.csv파일 읽어서
# 가격 ,(천단위) 제거한 후 float변환
# 이름,가격을 3줄만 출력
f = open('day02\\apt_201910.csv', 'r')
reader = csv.reader(f)
output = []
for i in reader :
  output.append(i)

for i in output :
  for j in i :
    try :
      i[i.index(j)] = float(re.sub(',','',j))
    except :
      pass

print(output[:3])

# 강원도에 120m2 이상, 3억 이하 검색해서 시군구 단지명 가격 출력하기
new_list = [['시군구', '단지명', '가격']]
for i in output :
  try : 
    if i[5] >= 120 and i[-4] <= 30000 and re.match('강원', i[0]) :
      new_list.append([i[0], i[4], i[-4]])
  except :
    pass
print(new_list)

# csv이용해서 내보내기
with open('day02\\apt_201910_out.csv', 'w', newline='', encoding='utf-8') as f :
  a = csv.writer(f)
  a.writerows(new_list)