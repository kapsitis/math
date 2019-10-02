from pylab import *
import numpy as np

x = np.random.random(50)
y = np.random.random(50)
c = np.random.random(50)  # color of points
s = 500 * np.random.random(50)  # size of points

fig, ax = subplots()
im = ax.scatter(x, y, c=c, s=s, cmap=cm.jet)

# Add a colorbar
fig.colorbar(im, ax=ax)

# set the color limits - not necessary here, but good to know how.
im.set_clim(0.0, 1.0)

show()