def multi(num1, num2) :
  return num1 + num2, num1 - num2

hap, sub = multi(100, 200)
print(f"multi()에서 리턴한 값 {hap}, {sub}")
print("multi()에서 리턴한 값 %d, %d" % (hap,sub))

