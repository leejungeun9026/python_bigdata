def seperate() :
  a = int(input('수 입력 >> '))
  if a % 2 == 0 :
    print("짝수")
  else :
    print("홀수")
# 함수 출력
# seperate()


def addReturn(num1, num2) :
  return num1 + num2

sum = addReturn(3, 5)
print("addReturn의 결과 : ", sum)
print("addReturn의 결과 : ", addReturn(11, 13))


# 1부터 num까지의 합 계산
def hap(num) :
  sum = 0
  for i in range(1, num+1) :
    sum += i
  return sum
print(hap(10))
print(hap(100))


# 함수만들기
def max_count(nums) :
  dict1 = {}
  key = set(nums)
  for i in key :
    dict1[i] = nums.count(i)
  return dict1

def max_count2(nums) :
  counts_dic = {}
  for i in nums:
    if i in counts_dic :
      counts_dic[i] += 1
    else :
      counts_dic[i] = 1
  return counts_dic


nums = [1, 1, 1, 2, 2, 3, 2, 3, 2, 3, 3, 3, 1]

counts = max_count(nums)
print(counts)

counts2 = max_count2(nums)
print(counts2)


# counts dic에서 최대 value 값
counts_max = max(counts.values())
print("counts_dic에서 최대 value 값: ", counts_max)

# counts dic 최대 value의 key 값
for k, v in counts.items() :
  if v == counts_max :
    print("counts dic 최대 value의 key 값 : ", k)