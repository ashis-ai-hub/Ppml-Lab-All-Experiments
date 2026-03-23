import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[5,7,6,8,7]
plt.scatter(x,y,c='b',label="Scatter Plot")
plt.title("Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.show()
categories=['A','B','C','D']
values=[3,7,8,5]
plt.bar(categories,values=values,c='g',label="Bar data")
plt.title("Bar plot")
plt.xlabel("categories")
plt.ylabel("value")
plt.legend()
plt.show()