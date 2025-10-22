import pandas as pd

##### ✅ 데이터 전처리 ######
# 1. 파일 읽기
red_df = pd.read_csv('day08/winequality-red.csv', sep=';', header=0, engine='python')
white_df = pd.read_csv('day08/winequality-white.csv', sep=';', header=0, engine='python')


# 2. 구분자를 ,로 바꿔서 저장하기
red_df.to_csv('day08/winequality-red2.csv', index=False)
white_df.to_csv('day08/winequality-white2.csv', index=False)

print(red_df.head())


# 3. type column 추가하여 값 넣기
red_df.insert(0, column='type', value='red')
print(red_df.head())
print(red_df.shape) # (1599, 13)

white_df.insert(0, column='type', value='white')
print(white_df.head())
print(white_df.shape) # (4898, 13)


# 4. red, white파일 병합하기(concat)
wine = pd.concat([red_df, white_df])
print(wine.shape) # (6497, 13)


# 5. 병합한 파일(wine.csv) 내보내기
wine.to_csv('day08\\wine.csv', index=False)





##### ✅ 데이터 탐색 ######
# 1. 기본 정보 확인
print(wine.info())


# 2. column명 변경
wine.columns = wine.columns.str.replace(" ", "_")
print(wine.head())
# describe() : 데이터 요약 통계(count, mean, min, max, ...등) 출력
print(wine.describe())


# 3. quality의 unique값 출력
# - unique() : 중복된 값을 제거하고, 유일한(unique) 값들만 반환하는 함수
# - value_counts() : 유일한(unique) 값 + 갯수를 반환하는 함수

print(wine.quality.unique())
# [5 6 7 4 8 3 9]

print(sorted(wine.quality.unique()))
# [np.int64(3), np.int64(4), np.int64(5), np.int64(6), np.int64(7), np.int64(8), np.int64(9)]

print(wine.quality.value_counts())





##### ✅ 데이터 모델링 ######
# 1. 그룹 비교1: describe() 함수 이용
# type을 기준으로 그룹을 나눈 뒤 quality속성을 기준으로 기술통계를 구함
print('\n===== describe =====')
print(wine.groupby('type')['quality'].describe())

print('\n===== mean =====')
print(wine.groupby('type')['quality'].mean()) # 평균

print('\n===== std =====')
print(wine.groupby('type')['quality'].std())  # 표준편차

print('\n===== agg (mean, std) =====')
print(wine.groupby('type')['quality'].agg(['mean', 'std'])) # 묶어서 한번에



# 2. 그룹 비교2 : t-검정(scipy), 회귀분석(statsmodels) 이용
# import 안되면 install 먼저 해야함 >>> pip install statsmodels
from scipy import stats
from statsmodels.formula.api import ols, glm

# type과 quality column만 담기
red_wine_quality = wine.loc[wine['type']=='red', 'quality']
white_wine_quality = wine.loc[wine['type']=='white', 'quality']

# t- 검정으로 그룹 간 차이 확인
print('\n===== red_wine_quality =====')
print(red_wine_quality.head())
print('\n===== white_wine_quality =====')
print(white_wine_quality.head())

stats_value = stats.ttest_ind(red_wine_quality, white_wine_quality)
print('\n===== stats_value =====')
print(stats_value)
# -> pvalue가 0.05보다 작으면 두 그룹은 차이가 있는걸로 판단함

# 회귀분석
Rformula = 'quality ~ fixed_acidity + volatile_acidity + citric_acid + residual_sugar + chlorides + free_sulfur_dioxide + total_sulfur_dioxide + density + pH + sulphates + alcohol'
regression_result = ols(Rformula, data=wine).fit()

print('\n===== stats_value =====')
print(regression_result.summary())



# 3. 회귀분석 모델로 새로운 품질 등급 예측하기
sample1 = wine[wine.columns.difference(['quality', 'type'])]
sample1 = sample1[0:5][:]
print('\n===== sample1 =====')
print(sample1)
sample1_predict = regression_result.predict(sample1)
print('\n===== sample1 vs wine =====')
print(sample1_predict)
print(wine[0:5]['quality'])

# 두번째 예측에 사용할 샘플 데이터 만들기
data = {"fixed_acidity" : [8.5, 8.1], "volatile_acidity":[0.8, 0.5],
"citric_acid":[0.3, 0.4], "residual_sugar":[6.1, 5.8], "chlorides":[0.055,
0.04], "free_sulfur_dioxide":[30.0, 31.0], "total_sulfur_dioxide":[98.0,
99], "density":[0.996, 0.91], "pH":[3.25, 3.01], "sulphates":[0.4, 0.35],
"alcohol":[9.0, 0.88]}

sample2 = pd.DataFrame(data, columns=sample1.columns)
print('\n===== sample2 =====')
print(sample2)

sample2_predict = regression_result.predict(sample2)
print(sample2_predict)





##### ✅ 시각화 ######
# 1. 와인 유형에 따른 품질 등급 히스토그램 그리기
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('dark')
sns.histplot(red_wine_quality, stat='density', kde=True, color='red', label='red wine')
sns.histplot(white_wine_quality, stat='density', kde=True, label='white wine')
plt.title('Quality of Wine Type')
plt.legend()
plt.show()

import statsmodels.api as sm

others = list(set(wine.columns).difference(set(["quality", "fixed_acidify"])))
p, resids = sm.graphics.plot_partregress("quality", "fixed_acidity", others, data=wine, ret_coords=True)
plt.show()
fig = plt.figure(figsize=(8, 13))
sm.graphics.plot_partregress_grid(regression_result, fig=fig)
plt.show()