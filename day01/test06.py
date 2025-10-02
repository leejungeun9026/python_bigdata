text = "<title>지금은 문자열 연습입니다.</title>"
print(text[0:7])
# find() 문자열의 위치값 인덱스를 리턴, 📌없으면 -1 리턴
print(text.find("문"))
print(text.find("파"))
# index() 문자열의 위치값 인덱스를 리턴, 📌없으면 오류 발생
print(text.index("문"))
# print(text.index("파"))

text1 = "    <title>지금은 문자열 연습입니다.</title>       "
print(text1)
print(len(text1))         # 공백 제거 전 길이 출력
print(len(text1.strip())) # 공백 제거 후 길이 출력
print(len(text1))         # 공백 제거 전 길이 출력
print(len(text1.lstrip()))
print(len(text1.rstrip()))

text2 = ";"
print(text1 + text2)

print(text.replace("<title>", "<div>"))
print(text.replace("title", "div"))

up = text.upper()
print(up)
print(up.lower())



# 정규식 표현
# import re : 정규 표현식을 지원하는 모듈

# 메타문자(의미를 가지는 문자) : . ^ $ * + ? { } [ ] \ | ( ) 
# [0-9] : 모든 숫자 (0부터 9까지)
# [a-z] : 모든 소문자 알파벳
# [a-zA-Z] : 모든 알파벳 (소문자와 대문자 모두)

# * : 바로 앞에 있는 문자가 0부터 무한대까지 반복될 수 있다는 의미
# ab*c => ac, abc, abbc, abbbbc

# + : 앞에 있는 문자가 최소 1번 이상 반복될 때 사용
# ab+c : ac(안됨), abc, abbc

# .(dot) : 모든 문자와 매치된다는 것을 의미 (줄바꿈 문자인 \n 제외)
# a.b : aab, a0b => "a + 모든_문자 + b"

# ? : 앞의 문자가 있어도 되고 없어도 됨
# ab?c : ac, abc => "a + b가_있어도_되고_없어도_됨 + c"

import re
text3 = "<head>안녕하세요</head>"
body = re.search('<head.*/head>', text3)
print(body)
body = body.group()
print(body)


text4 = ("<head>안녕하세요...<title>지금은 문자열 연습</title></head>")
body = re.search("<title.*/title>" ,text4)
print(body)
body = body.group()
print("body : ", body)

body1 = re.search("<.+?>" , body)
print("body1 : ", body1.group())

body2 = re.search("<.+>" , body)
print("body2 : ", body2.group())

body3 = re.sub("<.+?>", "", body) #sub("제외할 문자", "대체할 문자", 대상)
print("body3 : ", body3)



############################
a = [1, 2, 3, 4, 5, 2, 2]
print(a)
print(set(a))
print(type(set(a)))