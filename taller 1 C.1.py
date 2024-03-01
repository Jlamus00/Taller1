import numpy as np
import matplotlib.pyplot as plt

x =([-200,-150,-100,-50,0,50,100,150,200])
y=([23,42.2,61.5,80.7,100,119.2,138.5,157.7,177])
plt.plot(x,y,'b-o')
plt.xlabel('temperatura(°C)')
plt.ylabel('Resistencia(Ohms)')
plt.title('PT100')
plt.show()