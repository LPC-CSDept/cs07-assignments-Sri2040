import matplotlib.pyplot as plt
import numpy as np


labels = ['Bill', 'Jim', 'Joe']
math = [100, 100, 100]
science = [90, 90, 80]
english = [90, 90, 90]
computer = [90, 80, 90]

x = np.arange(len(labels))
width = 0.15

fig, ax = plt.subplots()
rects1 = ax.bar(x - width*1.5, math, width, label='Math')
rects2 = ax.bar(x - width*0.5, english, width, label='English')
rects3 = ax.bar(x + width*0.5, science, width, label='Science')
rects4 = ax.bar(x + width*1.5, computer, width, label='Computer')

ax.set_ylabel('Scores')
ax.set_title('Grouped graph for scores')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)
ax.bar_label(rects3, padding=3)
ax.bar_label(rects4, padding=3)

fig.tight_layout()

plt.show()