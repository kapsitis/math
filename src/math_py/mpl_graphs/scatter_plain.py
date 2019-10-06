import numpy as np 
import matplotlib.pyplot as plt 

a, b, N = 0., 1., 25
t = np.arange(a, b, (b-a)/N) 

# sarkana svītrlīnija 'r--'
# zili kvadrātiņi     'bs'
# zaļi trijstūrīši    'g^'
plt.plot(t, t, 'r--', 
        t, t**2, 'bs', 
        t, t**3, 'g^')
plt.savefig('scatter_plain.png')
plt.show()