# 1) 구구단 2~9단
for i in range(2, 10) :
  print(f"{i}단")
  for j in range(1, 10) :
    print(f"{i} x {j} = {i*j}")


# 2) 짝수만 출력
mylist = [3, 5, 4, 9, 2, 8, 2, 1]
evenlist = []
for i in mylist:
  if i % 2 == 0 :
    evenlist.append(i)

print(evenlist)

# 리스트 컴프리헨션 사용
# 리스트 컴프리헨션 : [표현식 for 항목 in 반복_가능_객체 if 조건문]
lst3 = [ i for i in mylist if i % 2 == 0 ]
print(lst3)


# 3) 19세 이상인 사람만 추출하여 adult리스트에 저장 (리스트 컴프리헨션 사용)
people = [31, 53, 41, 19, 15, 18, 21, 13]
adult = [ i for i in people if i >= 19 ]
print(adult)


# 4) 항목이 2개인 것만 추출하여 newlist에 저장
mylist = [[1, 2], [3, 4, 5], [6, 7]]
newlist = [ i for i in mylist if len(i) == 2 ]
print(newlist)