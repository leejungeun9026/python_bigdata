import re
import csv
import usecsv

output_result = usecsv.opencsv('day02\\apt_201910.csv')
output = usecsv.deletecoma(output_result)

# 강원도에 120m2 이상, 3억 이하 검색해서 시군구 단지명 가격 출력하기
new_list = [['시군구', '단지명', '가격']]
for i in output :
  try : 
    if i[5] >= 120 and i[-4] <= 30000 and re.match('부산', i[0]) :
      new_list.append([i[0], i[4], i[-4]])
  except :
    pass
print(new_list)

# csv이용해서 내보내기
with open('day02\\apt_201910_out2.csv', 'w', newline='', encoding='utf-8') as f :
  a = csv.writer(f)
  a.writerows(new_list)