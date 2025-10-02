# singer1.csv 파일을 읽어서
# 키가 165 이상인 사람 이름, 평균키를 출력하여
# singer1_out.csv파일로 내보내기

with open('day02\\singer1.csv','r') as inFp:
  with open('day02\\singer1_out.csv', 'w', encoding='utf-8') as outFp:
    header = inFp.readline()
    header = header.strip()
    header_list = header.split(',')
    height_idx = header_list.index('평균 키')
    name_idx = header_list.index('이름')

    output=[]
    for data in inFp :
      dataStr = data.strip()
      row_list = data.split(',')
      if int(row_list[height_idx]) >= 165 :
        output.append([row_list[name_idx], row_list[height_idx]])

    # 리스트를 문자열로 변환
    row_str = ','.join(map(str, output))
    outFp.write(row_str)