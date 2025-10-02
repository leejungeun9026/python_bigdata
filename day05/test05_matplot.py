import matplotlib.pyplot as plt

# add_subplot('특정 위치')
# add_subplot([총 행위 수], [총 열의 수], [subplot 번호])

figure = plt.figure()

axes1 = figure.add_subplot(2, 2, 1)
axes2 = figure.add_subplot(2, 2, 2)
axes3 = figure.add_subplot(2, 2, 3)
axes4 = figure.add_subplot(2, 2, 4)
axes1.plot([0,2])
axes2.plot([1,1])
axes3.plot([2,0])
axes4.plot([1,2])
plt.show()


###
# subplots() : figure와 subplot을 동시에 생성함
# subplots(생성할 subplot 행, 열)
figure, axes = plt.subplots(2, 2) #0,0, 0,1 1,0 1,1
axes[0][0].plot([1,1])
axes[1][1].plot([1,2])
plt.show()


###
figure = plt.figure()
axes = figure.add_subplot(224)
x = [0, 2, 4, 6]
y = [0, 4, 0, 2]
x2 = [0, 1, 2, 3, 4, 5, 6]
y2 = [1, 2, 3, 4, 5, 6, 7]
axes.plot(x, y, color='r', linestyle='dashed', marker='^')
axes.plot(x2, y2, color='k', linestyle='dashed', marker='o')
plt.show()



###
figure = plt.figure()
axes = figure.add_subplot(111)
x = [1, 2, 3, 4]
y = [1, 4, 0, 2]
x2 = [11, 12, 13, 14]
y2 = [11, 14, 13, 122]
axes.bar(x,y)
axes.bar(x2,y2)
plt.show()