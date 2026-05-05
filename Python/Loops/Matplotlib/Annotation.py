import matplotlib.pyplot as plt
import numpy as np
time = [0, 1, 2, 3, 4, 5]
temp = [30, 32, 34, 35, 33, 31]
plt.plot(time, temp)
plt.annotate('Peak', xy=(3,35) , xytext=(4, 36), arrowprops=dict(facecolor='black', shrink=0.05))
plt.show()