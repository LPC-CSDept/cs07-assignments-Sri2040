import numpy as np
import matplotlib.pyplot as plt
data = [[30, 25],[40, 23],[35, 22],[10,10]]
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
x = np.arange(2)
ax.bar(x + 0.00, data[0], color = 'b', width = 0.25)
ax.bar(x + 0.25, data[1], color = 'orange', width = 0.25)
ax.bar(x + 0.50, data[2], color = 'r', width = 0.25)
ax.bar(x + 0.75, data[3], color = 'g', width = 0.25)
plt.show()