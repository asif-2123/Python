import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(100)

plt.subplot(1,2,1)
plt.hist(data)
plt.title("Histogram")

plt.subplot(1,2,2)
plt.boxplot(data)
plt.title("Boxplot")

plt.show()