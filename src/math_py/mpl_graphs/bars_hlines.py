from pylab import *
y = arange(0,3,0.1)
x = 2*y
hlines(y, 0, x, color='b', lw=4)
savefig('bars_hlines.png')
show()
