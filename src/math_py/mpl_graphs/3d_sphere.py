from numpy import *
import pylab as p
import mpl_toolkits.mplot3d.axes3d as p3

u=r_[0:2*pi:100j]
v=r_[0:pi:100j]

x=10*outer(cos(u),sin(v))
y=10*outer(sin(u),sin(v))
z=10*outer(ones(size(u)),cos(v))

fig=p.figure()
ax = p3.Axes3D(fig)
ax.plot_wireframe(x,y,z)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

p.savefig('3d_sphere.png')
p.show()
