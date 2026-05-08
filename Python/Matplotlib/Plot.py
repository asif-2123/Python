import matplotlib.pyplot as plt
import numpy as np

time = [0, 1, 2, 3, 4, 5]
temperature = [30, 32, 31, 29, 28, 27]
plt.plot(time, temperature, marker='o',linestyle='dashdot', color='red')
plt.title('Temperature over Time')
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.grid(True)
plt.legend(['Temperature'])
plt.show()