import pandas as pd

# pandas로 데이터 파일 읽기
df = pd.read_csv('day02\\apt_201910.csv', encoding='cp949', thousands=',')

# 타입 확인 
print(type(df)) # => DafaFrame자료형
# DafaFrame 길이 출력
print(len(df))  # => 42758 : 행 출력
# shape : DafaFrame 행렬 모양 출력
print(df.shape) # (42758, 12) : 42758행, 12열
# head : DafaFrame 위에서부터 5개 행 출력
print(df.head())
# tile : DafaFrame 아래에서부터 5개 행 출력
print(df.tail())
# [], . : DafaFrame 열을 지정해서 출력
print(df['면적'])
print(df.면적)

# 면적이 200보다 큰 경우만 출력
print(df[df['면적'] > 200])

# loc(행범위, 열이름) : 원하는 행과 열만 출력
print(df.loc[:, ['단지명', '가격']])
print(df.loc[:10, ('단지명', '가격')])

# 가격을 위에서 5개 출력
print(df.가격.head())
print(df['가격'].head())
# 면적이 130 넘는 아파트의 가격만 출력
print(df.가격[df['면적'] > 130])

print('-'*30)

# 면적이 130이 넘고 가격이 2억 미만인 아파트의 가격 출력
print(df.가격[(df.면적>130) & (df.가격<20000)])

print(df.가격[(df.면적>130) | (df.가격<20000)].head())

# 가격 내림차순 정렬
df_desc = df.sort_values(by='가격', ascending=False)
print(df_desc.가격)


# 9억원 초과하는 가격으로 거래된 단지명과 가격 출력
print(df.loc[ df.가격 > 90000 , ['단지명', '가격']])
print(df.loc[:, ['단지명', '가격']][df.가격 > 90000])

# 단가 컬럼 생성
# 없는 컬럼을 생성할때는 ['컬럼명']사용
df.단가 = df.가격/df.면적
print(df.단가)
df['단가'] = df.가격/df.면적
print(df.단가)

print(df.loc[:10, ('시군구', '면적', '단가')])


# 파일 내보내기
df1 = df.loc[:10, ('시군구', '면적', '단가')]
df1.to_csv('day02/apt_df.csv', index=False)


##########################################
data_dic = {
  'name' : ['aaa', 'bbb', 'ccc', 'ddd'],
  'age' : [22, 33, 44, 55],
  'score' : [97.2, 55.6, 33.5, 22.9]
}
# dic ==> DataFrame으로 
df2 = pd.DataFrame(data_dic)
print(df2)
print(type(df2))
print(df2.sum())
print(df2['age'].mean())