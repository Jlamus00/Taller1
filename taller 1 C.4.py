import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


x = float(input("Ingrese la coordenada x: "))
y = float(input("Ingrese la coordenada y: "))
z = float(input("Ingrese la coordenada z: "))


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.quiver(0, 0, 0, x, y, z)

ax.set_xlim([0, max(x, 1)])
ax.set_ylim([0, max(y, 1)])
ax.set_zlim([0, max(z, 1)])


plt.show()


