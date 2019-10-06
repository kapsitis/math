# -*- coding: utf-8 -*-
import numpy as np 
import matplotlib.pyplot as plt 

N = 10000
mu, sigma = 175, 7 
x = mu + sigma * np.random.randn(N) 

plt.hist(x, 50, density=True, 
        facecolor='g', alpha=0.75, ec='#000088') 
plt.xlabel('Garums (cm)') 
plt.ylabel('Varbūtība') 
plt.title('%d cilvēku garums; μ=%d, σ=%d' % (N,mu,sigma)) 
plt.text(60, .025, r'$\mu=%d,\ \sigma=%d$' % (mu,sigma)) 
plt.axis([140, 210, 0, 0.07]) 
plt.grid(True) 

plt.savefig('bars_histogram_separated.png')
plt.show()