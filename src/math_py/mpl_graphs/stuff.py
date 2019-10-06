import numpy as np 
import matplotlib.pyplot as plt 

y = np.arange(0,3,0.1)
x = 2*y
plt.hlines(y, 0, x, color='b', lw=4)
plt.savefig('bars_hlines.png')
plt.show()