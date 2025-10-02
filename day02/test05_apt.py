import re

# apt_201910.csv파일 읽어서
# 가격 ,(천단위) 제거한 후 float변환
# 이름,가격을 3줄만 출력
with open('day02\\apt_201910.csv', 'r') as inFp:
  header = inFp.readline()
  header = header.strip()
  header_list = header.split(',')
  name_idx = header_list.index('단지명')
  price_idx = header_list.index('가격')

  output = []
  for data in inFp :
    row = data.strip()
    row_list = data.split(',')

    output.append([row_list[name_idx]])
  print(output[:3])

