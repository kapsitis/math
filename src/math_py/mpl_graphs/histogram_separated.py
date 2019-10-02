import numpy as np 
import matplotlib.pyplot as plt 

## https://biology.stackexchange.com/questions/9730/what-is-the-standard-deviation-of-adult-human-heights-for-males-and-females

mu, sigma = 175, 7 
x = mu + sigma * np.random.randn(10000) 

# the histogram of the data 
n, bins, patches = plt.hist(x, 50, density=True, facecolor='g', alpha=0.75, ec='white') 

plt.xlabel('Height') 
plt.ylabel('Probability') 
plt.title('Human height') 
plt.text(60, .025, r'$\mu=%d,\ \sigma=%d$' % (mu,sigma)) 
plt.axis([140, 210, 0, 0.07]) 
plt.grid(True) 

plt.savefig('histogram_separated.png')
plt.show()