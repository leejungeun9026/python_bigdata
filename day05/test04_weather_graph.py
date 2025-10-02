import pandas as pd

df = pd.read_csv('day05\\weather_1002.csv', encoding='utf-8-sig', index_col='지역')
print(df)

print(df.head())
# 서울, 인천, 대전, 대구, 광주, 부산
city_df = df.loc[['서울', '인천', '대전', '대구', '광주', '부산']]

##### 그래프 #####
import matplotlib.pyplot as plt
import matplotlib as mpl

# 한글
font_name = mpl.font_manager.FontProperties(fname='c:/Windows/fonts/malgun.ttf').get_name()
mpl.rc('font', family=font_name)

ax = city_df.plot(kind='bar', title='날씨', figsize=(9,6), fontsize=12, legend=True)
ax.set_xlabel('도시')
ax.set_ylabel(['기온', '습도'])
plt.show()


############
figure = plt.figure()
axes = figure.add_subplot(111)
xdata = ['서울', '인천', '대전', '대구', '광주', '부산']
axes.bar(xdata, city_df['현재 기온'], label='기온')
plt.legend(['기온'])
plt.show()

axes2 = figure.add_subplot(122)
axes2.bar(xdata, city_df['습도'])
plt.show()

figure = plt.figure()
axes = figure.add_subplot(111)
axes.plot(xdata, city_df['현재 기온'])
axes.plot(xdata, city_df['습도'])
plt.legend(['기온'])
plt.legend()
plt.show()