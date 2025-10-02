# numpy
# - 수치데이터를 다루기 위한 라이브러리
# - 선형대수 계산 등 행렬 연산에 주로 사용됨
# - 다차원 배열 구조인 ndarry 지원

# pandas
# - 데이터분석에서 자주 사용
# - 테이블 형태를 다루는 라이브러리
# 1차원 자료 구조 : Series
# 2차원 자료 구조 : DataFrame
# 3차워 자료 구조 : Panel

import numpy as np
# 아나콘다가 아닌 그냥 파이썬일 경우 설치 필요
# 설치 명령어 : pip install numpy

a = np.array([[2,3,4], [5,2,1]])
print(a)

d = np.array([2, 3, 4, 5, 6, 7])
print(d)
print("d.shape : ", d.shape)
print("d.dtype : ", d.dtype)
print(a.shape)

e = np.array([[1, 2, 3, 4], [3, 4, 5, 6]])
print(e)
print("e.shape : ", e.shape)
print("e.dtype : ", e.dtype)

# 초기값과 구조를 지정하여 배열 생성
print(np.zeros((2, 10)))  # 초기값 : 0
print(np.ones((2, 10)))   # 초기값 : 1
print(np.arange(2,10))    # 2이상 10미만의 원소로 이루어진 1차 배열

print(np.zeros((2, 2, 5)))


# 1로 이루어진 2행 3열의 a배열 생성
a = np.ones((2, 3))
print(a)
# transpose 행과 열이 바뀜
b = np.transpose(a)
print(b)

arr1 = np.array([[2, 3, 4], [6, 7, 8]])
arr2 = np.array([[12, 13, 14], [26, 27, 28]])
print("arr1\n", arr1)
print("arr2\n", arr2)

# 배열 연산 : 같은 자리 원소끼리 연산
print("배열 덧셈\n", arr1+arr2)
print("배열 뺄셈\n", arr1-arr2)
print("배열 곱셈\n", arr1*arr2)
print("배열 나눗셈\n", arr1/arr2)


# list와 차이점
d_list = [[1, 2, 3, 4, 5],[2, 3, 4, 5, 6, 7],[5, 6, 7, 8, 9, 9]]
print(d_list) # 출력 가능
print(type(d_list))
# d = np.array([[1, 2, 3, 4, 5],[2, 3, 4, 5, 6, 7],[5, 6, 7, 8, 9, 9]])
# => 오류 발생

print(d_list[:2])
# d_list[:2] = 0 리스트 범위 지정해서 수정 시 에러발생
d_list[2] = 0
print(d_list[2])

d_array = np.array([[1, 2, 3, 4, 5],[2, 3, 4, 5, 6],[5, 6, 7, 8, 9]])
d_array[:2] = 0
print(d_array)


print(np.arange(10))
arr4 = np.arange(10) + 1  # 각각의 원소에 1을 더함
print(arr4)
print(arr4[:5])
print(arr4[-3:])