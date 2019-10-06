import matplotlib.pyplot as plt 
import numpy as np

x = np.random.normal(2, 0.5, 100000)
plt.hist(x, bins=50)
plt.savefig('bars_histogram_plain.png')

plt.show()
