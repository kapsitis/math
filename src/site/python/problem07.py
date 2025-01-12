import sympy
import matplotlib.pyplot as plt

n = 2
primes = []
sum_values = []

for p in range(3, 200): 
    if sympy.isprime(p):
        primes.append(p)
        sum = 0
        # for k in range(1, (p-1)//2 + 1): 
        #     sum += k**2 % p
        for k in range(1, p):
            sum += k**2 % p        
        
        avg_sum = sum/ p**2
        sum_values.append(avg_sum)
        if avg_sum < 0.48:
            print(f'avg_sum({p}) = {avg_sum}')


# Create the scatter plot
plt.scatter(primes, sum_values, c='red', label='sum(p) / p^2')

# Add titles and labels
plt.xlabel('Prime Number (p)')
plt.ylabel('sum / p^2')
plt.title('Scatter Plot of sum / p^2 vs Prime Numbers')

# Display the plot
plt.legend()
plt.grid(True)
plt.show()
