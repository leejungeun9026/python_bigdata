import csv
import re

# 파일 불러오기
# 파일 오픈 및 읽기모드
f = open('day02\\popSeoul.csv', 'r')

# csv함수로 가져온 쉽게 읽기
reader = csv.reader(f)
print(reader)
# => 오브젝트 출력됨 <_csv.reader object at 0x000001255583B100>

# 할 일
# 1. 리스트 만들어서 한줄씩 담기
# 2. 숫자 ,(천단위) 제거하기
# 3. 문자를 숫자(float)으로 변환하기
output = []
for i in reader :
  tmp = []
  for j in i :
    if re.search(r'\d', j) :
      # 숫자 찾아서 
      # 쉼표 제거, 숫자로 형변환, tmp리스트에 담기
      tmp.append(float(re.sub(',','', j)))
    else :
      # 숫자가 아니면 tmp 리스트에 그냥 넣기
      tmp.append(j)
  output.append(tmp)
print(output)

# 외국인 비율이 5% 이상인 결과만 리스트로 출력하기
# 내가 한거
print("-"*30)
lst1 = []
for i in range(1, len(output) - 1) :
  korean = int(output[i][1])
  foreign = int(output[i][2])
  percent = foreign/(korean+foreign) * 100
  if percent > 5 :
    lst1.append(output[i])
print(lst1)

# 선생님이 한거
print("-"*30)
result = [['구', '한국인', '외국인', '외국인 비율(%)']]
for i in output :
  try : 
    foreign = round(i[2]/(i[1]+i[2]) * 100,1 )
    if foreign > 5 :
      result.append([i[0], i[1], i[2], foreign])
  except :
    pass
print(result)

# csv 라이브러리 이용
# with open('foreign.csv', 'w', newline='') as f :
#   a = csv.writer(f, delimiter=',')
#   a.writerows(result)

# csv 라이브러리 이용X
# result -> 문자열로 변환 필요(map사용)
# row_str = ','.join(map(str,result))
# with open('foreign2.csv', 'w', newline='') as f :
#   f.write(row_str + "\n")
