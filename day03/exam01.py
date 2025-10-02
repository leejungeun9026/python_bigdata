# 1. pandas 이용해서 singer2.csv 읽기
# 유튜브 조회수 300000 이상인 데이터 출력
import pandas as pd

# encoding utf-8이 오류발생하면 아마 옛날버전?이므로 cp949
df = pd.read_csv('day03\\singer2.csv', encoding='cp949', thousands=',')
print(df[df['유튜브 조회수'] > 300000])





# 2. 1~10까지 합 출력
sum = 0
for i in range(11) :
  sum += i
print("sum = " , sum)





# 3. 구구단(2~9단) 출력
for i in range(2, 10) :
  print(i, "단")
  for j in range(1, 10) :
    print(f"{i} X {j} = {i*j}")
  print()





# 4. 년도만 출력
import re 

exam = "저는 92년에 태어났습니다. 88년에는 올림픽이 있었습니다. 지금은 2025년입니다."
year = re.findall(r'[0-9]{0,2}[0-9][0-9]', exam)
year2 = re.findall(r'\d+년',exam)   # 숫자만 반복
year3 = re.findall(r'\d.+년',exam)  # 숫자 뒤의 모든 문자 반복
year4 = re.findall(r'\d.+?년',exam) # 숫자 뒤의 모든 문자인데..?

print(year)
print(year2)
print(year3)
print(year4)





# 5. .으로 구분하여 문장 출력
d = "I have a dog. I am not a girl. Yoi are not alone. I am happy"
rst1 = d.split('.')       # 파이썬 내장함수
rst2 = re.split('\.', d)  # re함수
print(rst1)
print(rst2)





# 6. mylist에서 짝수만 출력
mylist = [3, 5, 4, 9, 2, 8, 2, 1]
evenlist = [i for i in mylist if i % 2 == 0]
print(evenlist)





# 7. animals 리스트에서 새가 저장되어 있는 위치값 출력
animals = ['새', '코끼리', '강아지', '새', '강아지', '새']

# 내 답안
animals_index = []
index = 0
for i in animals :
  if (i == '새') :
    animals_index.append(index)
  index+=1
print(animals_index)

# 선생님1
animals_index2 = []
for i in range(len(animals)) :
  if (animals[i] == '새') :
    animals_index2.append(i)
print(animals_index2)

# 선생님2
animals_index3 = []
for i, animal in enumerate(animals) :
  if(animal == '새') :
    animals_index3.append(i)
print(animals_index3)





# 8. 문자열 chars에서 무작위로 5번 추출 -> 새로운 변수 pw에 삽입
import random
pw = str()
chars = '한글우수'

# i가 사용되지 않음(의미가 없으면) _로 표시 가능
for _ in range(5) :
  pw = pw + random.choice(chars)
print(pw)





# 9. survey.csv파일 위에서 5개 출력
survey = pd.read_csv('day03\\survey.csv', encoding='cp949', thousands=',')
rst9 = survey.head()
print(rst9)

# 스트레스지수의 평균
print(rst9.stress.mean())

# income의 합계
print(rst9.income.sum())

# income의 중앙값
print(rst9.income.median())

# 통계치 출력
print(rst9.describe())
print(rst9.income.describe())

# 그룹화 한 뒤 갯수 출력
print(rst9.sex.value_counts())
