import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
data = np.random.randn(100)
sns.kdeplot(data)
plt.show()
sns.distplot(data)
plt.show()