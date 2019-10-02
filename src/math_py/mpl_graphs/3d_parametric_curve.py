import sys

## https://mpl_graphs.org/3.1.0/faq/troubleshooting_faq.html
import matplotlib as mpl

from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

print(sys.version)
print('mpl_graphs.__version__ = %s' % mpl.__version__)
print('mpl_graphs.__file__ = %s' % mpl.__file__)


mpl.rcParams['legend.fontsize'] = 10
fig = plt.figure()

ax = fig.gca(projection='3d')
theta = np.linspace(-4 * np.pi, 4 * np.pi, 200)
z = np.linspace(-2, 2, 200)
r = z**2 + 1
x = r * np.sin(2*theta)
y = r * np.cos(2*theta)
ax.plot(x, y, z, label='parametric curve')
ax.legend()
plt.show()

plt.savefig('3d_parametric_curve.png')
plt.close(fig)
#mpimg.imsave(,fig)


