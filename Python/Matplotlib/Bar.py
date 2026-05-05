import pandas as pd
import matplotlib.pyplot as plt

s = pd.Series(['A','B','A','C','B','A'])

s.value_counts().plot(kind='bar')
plt.title("Category Count")
plt.legend()
plt.show()