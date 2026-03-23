import matplotlib.pyplot as plt
x = [1,2,3,4]
y = [10,20,30,40]
plt.plot(x,y)
plt.title("simple line plot")
plt.plot(x,y,linestyle='--',color = 'r',marker = '0',label = 'DataLine')
plt.xlabel("x_axis")
plt.ylabel("y_axis")
plt.legend()
plt.grid()
plt.show()