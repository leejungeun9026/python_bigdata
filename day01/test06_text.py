text = "<title>지금은 문자열 연습입니다.</title>"
print(text[0:7])
print(text.find('문'))  # 있다면 위치값 리턴
print(text.find('파'))  # 없으면 -1리턴
print(text.index('문'))  # 있다면 위치값 리턴
# print(text.index('파'))   # 없다면 오류발생

text1 = "    <title>지금은 문자열 연습입니다.</title>      "
print(text1)
print(len(text1))  #39
print(text1.strip()) # 양쪽공백 제거
print(len(text1.strip()))  #29
print(text1.lstrip())  # 왼쪽공백 제거
print(len(text1.lstrip())) # 35
print(text1.rstrip())  # 오른쪽공백 제거
print(len(text1.rstrip())) # 33

text2 = ";"
print(text1+text2)

print(text.replace('<title>','<div>'))
print(text.replace('<title>',''))
#대문자
up = text.upper()
print(up)
print(up.lower())

import re

text3 = "<head>안녕하세요</head>"
body = re.search('<head.*/head>', text3)
print('re.search : ',body)
body = body.group()
print('re.search : ',body)
# [0-9], [a-z]
# ab*c :  abc, abbc, abbbbbc,
# *(0번이상)  , +(1번이상) ?(0이상1이하)

print('-------------')
text4 = ('<head>안녕하세요... <title>지금은 문자열 연습</title></head>')
body = re.search('<title.*/title>', text4)
print(body)
body = body.group()
print(body)  # <title>지금은 문자열 연습</title>
body1 = re.search('<.+?>', body)
print('body1 : ', body1.group()) #<title>
body2 = re.search('<.+>', body) #<title>지금은 문자열 연습</title>
print('body2 : ', body2.group())
body3 = re.sub('<.+?>','', body)
print('body3 : ', body3)

###################
a = [1, 2, 3, 4, 5, 2, 2]
print(a)
print(set(a))
print(type(set(a)))

a = '제 이메일 주소는  greate@naver.com'
a += ' 오늘은  today@naver.com 내일은 apple@gmail.com  life@abc.co.kr 라는 메일을 사용합니다.'
print(a)
# 메일주소만 출력
mailText  =  re.findall(r'[a-z]+@[a-z.]+', a)
print('메일주소 출력 mailText: ' ,mailText)

words = ['apple', 'cat', 'brave', 'drama', 'asise', 'blow', 'coat', 'above']
# a로 시작하는 단어 출력 
wordList = []
for i in words:
  wordList += re.findall(r'a[a-z]+', i)

print('~~~ a로 시작하는 단어: ',wordList)

for i in words:
  wordList2 = re.search(r'a[a-z]+', i)
  if wordList2:
    print(wordList2.group())
print()

for i in words:
  # wordList3 = re.match(r'a[a-z]+', i) # pattern을 문자열의 첫부분과 비교
  wordList3 = re.match(r'a\D+', i)  # \d(숫자) \D(숫자가 아닌)
  if wordList3:
    print(wordList3.group())