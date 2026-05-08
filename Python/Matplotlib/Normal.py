import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 50)
y = np.sin(x)

plt.figure(figsize=(8,5))
plt.plot(x, y, color='blue', linestyle='--', marker='o', label='Sine Wave')

plt.title("Sine Graph")
plt.xlabel("X values")
plt.ylabel("Sin(X)")
plt.legend()
plt.grid(True)

plt.show()