import matplotlib.pyplot as plt
from scipy.stats import bernoulli

p = 2/3
# Initially all poll totals (values 0..100) are set to '0'
allPolls = [0] * 101

for i in range(0,1000):
    responses = bernoulli.rvs(p, size=100)
    allPolls[sum(responses)] += 1

#plt.bar(list(range(0,101)), allPolls)
#plt.show()


