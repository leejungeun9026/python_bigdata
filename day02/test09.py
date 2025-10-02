import pandas as pd
# dict 형태로 표현하고 DataFrame형태로 변환

# year  sales
# 2018  350
# 2019  400
# 2020  1050
# 2021  2000
# 2022  1000
# 2023  2500

dic = {
  'year' : [2018, 2019, 2020, 2021, 2022, 2023],
  'sales' : [350, 400, 1050, 2000, 1000, 2500]
}

df = pd.DataFrame(dic)
print(df)


################################
# DataFrame 만들기
df2 = pd.DataFrame([[89.2, 92.5, 90.8], [92.8, 89.9, 95.2]],
                    index = ['중간고사','기말고사'],
                    columns=['1반', '2반', '3반'])
print(df2)

df3 = pd.DataFrame([[20251101, 'Kim', 90, 80],
                    [20251102, 'Lee', 85, 80],
                    [20251103, 'Park', 50, 50],
                    [20251104, 'Han', 78, 75]],
                    columns=['학번', '이름', '중간고사', '기말고사'])
print(df3)

# df3 중간고사 합계 / df3 기말고사 합계
print(df3['중간고사'].sum())
print(df3.기말고사.sum())

# 총점 컬럼(중간고사+기말고사) 생성해서 총점 평균 출력
df3['총점'] = df3['중간고사'] + df3['기말고사']
df3['평균'] = df3['총점']/2
print(df3.총점)
print(df3.총점.mean())
print(df3)

#df3 파일로 내보내기 (df3_pandas.csv)
df3.to_csv('day02\\df3_pandas.csv', index=False)


df4 = pd.DataFrame([[20251101, 'Kim', 90, 80],
                    [20251102, 'Lee', 85, 80],
                    [20251103, 'Park', 50, 50],
                    [20251104, 'Han', 78, 75]])
df4.columns = ['학번', '이름', '시험1', '시험2']
print(df4)
print(df4.tail(2))


# df3 파일 읽기
df33 = pd.read_csv('day02\\df3_pandas.csv')
print(df33)

# 총점이 160이상인것만 출력
print(df33[df33.총점 > 160])