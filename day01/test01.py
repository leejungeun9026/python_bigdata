print('hello')

a = 0
print(a)
print(type(a))

b = "hell oworld"
print(b)
print(type(b))

c = "안녕하세요"

d="\'안녕하세요\'"
print(d)

print(b)
print(b[0])
print(b[-1])
e = '안녕하세요'

print(e[0:2])
print(e[1:3])
print(e[0:5:2]) #2는 스탭
print(e[:]) # 처음부터 끝까지



########## List ==> [] ##########
l = list()
print(l, type(l))

lst = [1, 2, 3]
print(lst, type(list))

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 55]
print(l, type(l))

print("l의 첫번째 값 = ", l[0])
print("배열길이 : ", len(l))
print("배열의 마지막 출력 : ", l[len(l)-1], " or ", l[-1])

# 배열 l의 첫번재 값 수정
l[0] = 99
print(l)
l[1] = [1, 2, 3]
print(l)

l[2] = "문자"
print(l)

l.append(999)
print(l)
l.remove(5)
print(l)


########## tuple ==> () ##########
t = tuple()
print(t, type(t))
t1 = (1, 2, 3)
print(t1)
print(t1[0], t1[0:2])

print(t1 + t1)

#t1의 첫번째를 5로 수정
# t1[0] = 5 -> 오류 발생, 튜플은 수정 불가
print(t1)


########## dictionary ==> {} ##########
d1 = dict()
print(d1, type(d1))

d = {'a':1, 'b':2, 'c':3, 'd':4}
print(d, type(d))
print(d['a'])
d['d'] = 33
print(d)
print(d['d'])

d1 = d.keys()
print("keys() : ", d1)
print("keys() type : ", type(d1))

dd1 = d.keys
print("keys : ", dd1)

d2 = d.values()
print("values() : ", d2)
print("values() type : ", type(d2))

dd2 = d.values
print("values : ", dd2)

d3 = d.items()
print("items() : ", d3)
print("items() type : ", type(d3))

dd3 = d.items
print("items : ", dd3)

print(list(d.keys()), type(list(d.keys())))
print(list(d.values()), type(list(d.values())))

d['c'] = 2
print(d)
print(set(d.values()))
print(type(set(d.values())))