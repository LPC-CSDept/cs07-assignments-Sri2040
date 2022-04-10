import matplotlib.pyplot as plt
  
x = ['Math', 'English', 'Physics', 'Computer']
y1 = [100, 90, 80, 80]
y2 = [90, 80, 70, 100]
  
plt.bar(x, y1, color='blue')
plt.bar(x, y2, bottom=y1, color='orange')
plt.legend(["Bill", "Mary"])
plt.show()