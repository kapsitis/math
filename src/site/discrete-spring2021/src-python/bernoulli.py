from scipy.stats import bernoulli
p = 2/3

# Find the expected value ('mean') and variance
mean, var = bernoulli.stats(p, moments='mv')
print('(E(X)={}, V(X)={}'.format(mean, var))

# Generate random responses (1=success, 0=failure)
responses = bernoulli.rvs(p, size=100)
# Count the successful Bernoulli trials
print('sum(responses) = {}'.format(sum(responses)))
