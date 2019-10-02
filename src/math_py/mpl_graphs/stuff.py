import matplotlib.pyplot as plt
import numpy as np
# matplotlib inline
x = np.random.normal(size = 1000)
plt.hist(x, density=True, bins=30,  ec='white')
plt.ylabel('Probability')

plt.show()