import numpy as np
#from pylab import *
import matplotlib.pyplot as plt

labels = ["Baseline", "System"]
data =   [3.75               , 4.75]
error =  [0.3497             , 0.3108]

xlocations = np.array(range(len(data)))+0.5
width = 0.5
plt.bar(xlocations, data, yerr=error, width=width)
plt.yticks(range(0, 8))
plt.xticks(xlocations + width/2, labels)
plt.xlim(0, xlocations[-1]+width*2)
plt.title("Average Ratings")

plt.savefig('bars_with_errors.png')
plt.show()

