
import numpy as np

# Inicializa los vectores
vector1 = np.array([1, 2, 3])
vector2 = np.array([4, 5, 6])

# Realiza la suma de los vectores
suma = vector1 + vector2
print("Suma:", suma)

# Realiza la resta de los vectores
resta = vector1 - vector2
print("Resta:", resta)

# Realiza el producto punto de los vectores
producto_punto = np.dot(vector1, vector2)
print("Producto punto:", producto_punto)

# Realiza el producto cruz de los vectores
if len(vector1) == 3 and len(vector2) == 3:
    producto_cruz = np.cross(vector1, vector2)
    print("Producto cruz:", producto_cruz)
else:
    print("El producto cruz solo se puede calcular para vectores de 3 dimensiones")

# Realiza la división de los vectores
division = vector1 / vector2
print("Division:", division)