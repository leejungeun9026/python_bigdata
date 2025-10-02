########## 조건문 ##########
a = 2
if (a == 1) :
  print(1)
else : 
  print('1 아님')

if (a == 1) :
  print(1)
elif (a == 2) :
  print(2)
else :
  print(3)

########## 반복문 ##########
for i in [1, 2, 3] :
  print(i, end="")
print()
for i in (4, 5, 6) :
  print(i)

for i in "안녕하세요" :
  print(i)

print("="*20)
num = 5
while num > 0 :
  print(num)
  num -= 1

#num이 6이면 end 출력 후 종료
num = 10
while(num > 5) :
  print(num, end=" ")
  if num == 6 :
    print("end")
  num -= 1

num = 10
while num > 0 :
  print(num)
  if num == 6 :
    print("end")
    break
  num -= 1


print('='*20)
nums = [1, 2, 3, 4, 5]
test = (3, 6, 7)
for i in nums :
  if i in test :
    print(i)

for i in range(10) :
  print(i, end=" ")
print()

print('='*40)
sum = 0
for i in range(1, 101) :
  if i % 7 == 0 :
    print(i, end=" ")
    sum += i
print("\n합=", sum)

# d1의 value의 최대값
d1 = {'a':1, 'b':2, 'c':3}
print(max(d1.values()))

print(d1.items())

for k, v in d1.items() :
  if v == max(d1.values()) :
    print(k)

for i in range(3) :
  for j in range(3) :
    print("*", end=" ")
  print()