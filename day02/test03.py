import csv
import re

# 함수 만들기
# 파일 읽어서 리스트로 반환
def opencsv(filename) :
  output = []
  f = open(filename, 'r')
  reader = csv.reader(f)
  for i in reader :
    output.append(i)
  return output

result = opencsv('day02\\popSeoul2.csv')
print(result)

# 5개만 출력하기
for i in result[:5] :
  print(i)

# 5개만 , 제거하기
for i in result[:5] :
  for j in i :
    try : 
      # index로 위치 찾기
      i[i.index(j)] = float(re.sub(',','',j))
    except :
      pass


print('-'*20)
print(result[:5])