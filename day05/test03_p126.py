##### 7번 문제 #####

import pandas as pd

y1 = [500, 450, 520, 610]
y2 = [690, 700, 820, 900]
y3 = [1100, 1030, 1200, 1380]
y4 = [1500, 1650, 1700, 1850]
y5 = [1990, 2020, 2300, 2420]
y6 = [1020, 1600, 2200, 2550]

df = pd.DataFrame([y1, y2, y3, y4, y5, y6], 
                  index=[2015, 2016, 2017, 2018, 2019, 2020], 
                  columns=['1분기','2분기','3분기','4분기'])
df.to_csv('day05\\saves.csv', header=True)



##### 8번 문제 #####
import matplotlib.pyplot as plt
x = range(len(y1))
xLabel = ['first', 'second', 'third', 'fourth']
plt.plot(x, y1, color="b")
plt.plot(x, y2, color="orange")
plt.plot(x, y3, color="green")
plt.plot(x, y4, color="red")
plt.plot(x, y5, color="purple")
plt.plot(x, y6, color="brown")
plt.xlabel('Quarters')
plt.ylabel('sales')
plt.title('2015~2020 Quarterly sales')
plt.xticks(x, xLabel, fontsize=10)
plt.legend(['2015', '2016', '2017', '2018', '2019', '2020'], loc='upper right')
plt.show()



##### 8-2 #####
df2 = pd.DataFrame([[500, 450, 520, 610],
                    [690, 700, 820, 900], 
                    [1100, 1030, 1200, 1380], 
                    [1500, 1650, 1700, 1850], 
                    [1990, 2020, 2300, 2420], 
                    [1020, 1600, 2200, 2550]],
                    index = [2015, 2016, 2017, 2018, 2019, 2020], 
                    columns=['1분기', '2분기', '3분기', '4분기'])

# transpose() : 행열 전환
df2 = df2.transpose()
print(df2)
df2.plot()
plt.show()
