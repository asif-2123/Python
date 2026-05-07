import matplotlib.pyplot as plt

data = [1,2,2,3,3,3,4,4,5]

plt.hist(data)
plt.title("Simple Histogram")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.show()