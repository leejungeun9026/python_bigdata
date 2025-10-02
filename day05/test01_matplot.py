import matplotlib.pyplot as plt

x = [1, 4, 9, 16, 25, 36, 49, 64]
# plt.plot(x)
# plt.show()

y = [i for i in range(1,9)]
# print(y)

plt.xlabel('x')
plt.ylabel('y')
plt.title('matplotlib sample')
plt.plot(x,y)
# plt.show()

y1 = [13, 16, 15, 18, 16, 17, 16]
plt.plot(y1)
plt.show()