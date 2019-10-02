from pylab import *
import numpy

x = numpy.random.normal(2, 0.5, 100000)
hist(x, bins=50)
savefig('dist_normal_histogram.png')

show()