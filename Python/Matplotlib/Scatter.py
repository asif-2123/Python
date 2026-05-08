import matplotlib.pyplot as plt
import pandas as pd

df=pd.DataFrame({
    'x':[1,2,3,4,5],
    'y':[2,3,5,7,11]
})

plt.scatter(df['x'], df['y'], color='blue', marker='o')
plt.title('Scatter Plot')
plt.xlabel('X values')  
plt.ylabel('Y values')
plt.grid(True)
plt.legend(['Data Points'])
plt.show()