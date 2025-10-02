import codecs
import re

f = codecs.open('day01\\friends101.txt', 'r', encoding='utf-8')
script101 = f.read()
print(script101[:100])

# Monica 대사 출력
monica = re.findall(r'Monica:.+', script101)
print(monica[:3])
print('type monica : ' , type(monica))

# All 대사 출력
all = re.findall(r'All:.+', script101)
print(all)

# All 마지막 대사
print(all[-1])
print(len(all))

# 출연진 몇명인지 출력하기
# actor = re.findall(r'.*:', script101)
# print(len(set(actor)))

# actor = re.findall(r'[A-Z][a-z]+:', script101)
# print(actor)

# 패턴 저장해놓기
pattern = re.compile(r'[A-Z][a-z]+:') # compile : 패턴 추출하는 함수
actor = re.findall(pattern, script101)
actor_set = set(actor)
print(actor_set, len(actor_set))

# :빼고 출력하기
actor2 = []
for i in actor_set :
  actor2.append(i[:-2])
print(actor2)

actor3 = []
for i in actor_set :
  actor3.append(re.sub(":", "", i))
actor3.sort()
print(actor3)

actor4 = []
for i in actor_set :
  actor4 += [i[:-2]]
print(actor4)