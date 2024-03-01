import matplotlib.pyplot as plt

# Coordenadas para la letra "d"
x_d = [0, 0, 0.5, 0.5, 0]
y_d = [1.5, 2.5, 2.25, 1.8, 1.5]

# Coordenadas para la letra "a"
x_a = [1.5, 1.5, 1, 1, 1.5]
y_a = [1.4, 2, 2, 1.5, 1.5 ]

# Coordenadas para la letra "y"
x_y = [2, 2, 2.5, 2.5, 2.5]
y_y = [2, 1.5, 1.5, 2, 1 ]

# Coordenadas para la letra "a"
x_a_1 = [3.5, 3, 3, 3.5, 3.5]
y_a_1 = [1.5, 1.5, 2, 2, 1.4 ]

# Coordenadas para la letra "n"
x_n = [4,4, 4.5, 4.5]
y_n = [1.5,2, 2, 1.5]

# Coordenadas para la letra "a"
x_a_2 = [5.5, 5.5, 5, 5, 5.5]
y_a_2 = [1.4, 2, 2, 1.5, 1.5]

# Crear la figura y el gráfico
fig, ax = plt.subplots()

# Graficar 
ax.plot(x_d, y_d, marker='o', linestyle='-')
ax.plot(x_a, y_a, marker='o', linestyle='-')
ax.plot(x_y, y_y, marker='o', linestyle='-')
ax.plot(x_a_1, y_a_1, marker='o', linestyle='-')
ax.plot(x_n, y_n, marker='o', linestyle='-')
ax.plot(x_a_2, y_a_2, marker='o', linestyle='-')

# Etiquetar los puntos"d"
for i, (xi, yi) in enumerate(zip(x_d, y_d)):
    ax.annotate(f'({xi},{yi})', (xi, yi), textcoords="offset points", xytext=(0,5), ha='center')

# Etiquetar los puntos"a"
for i, (xi, yi) in enumerate(zip(x_a, y_a)):
    ax.annotate(f'({xi},{yi})', (xi, yi), textcoords="offset points", xytext=(0,5), ha='center')

# Etiquetar los puntos"y"
for i, (xi, yi) in enumerate(zip(x_y, y_y)):
    ax.annotate(f'({xi},{yi})', (xi, yi), textcoords="offset points", xytext=(0,5), ha='center')

# Etiquetar los puntos"a"
for i, (xi, yi) in enumerate(zip(x_a_1, y_a_1)):
    ax.annotate(f'({xi},{yi})', (xi, yi), textcoords="offset points", xytext=(0,5), ha='center')

# Etiquetar los puntos"n"
for i, (xi, yi) in enumerate(zip(x_n, y_n)):
    ax.annotate(f'({xi},{yi})', (xi, yi), textcoords="offset points", xytext=(0,5), ha='center')

# Etiquetar los puntos"a"
for i, (xi, yi) in enumerate(zip(x_a_2, y_a_2)):
    ax.annotate(f'({xi},{yi})', (xi, yi), textcoords="offset points", xytext=(0,5), ha='center')

# Mostrar el gráfico 
plt.xlabel('Coordenada X')
plt.ylabel('Coordenada Y')
plt.title('Letra "e" con Coordenadas')
plt.grid(True)
plt.show()

#Siguiente nombre 
----------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt

# Coordenadas para la letra "L"
x_l = [0.5, 0, 0]
y_l = [1.5, 1.5, 2.5]

# Coordenadas para la letra "a"
x_a = [1.5, 1.5, 1, 1, 1.5]
y_a = [1.4, 2, 2, 1.5, 1.5 ]

# Coordenadas para la letra "m"
x_m = [3,3, 2.5, 2.5, 2.5, 2, 2]
y_m = [1.5, 2, 2, 1.5, 2, 2, 1.5]

# Coordenadas para la letra "u"
x_u = [4, 4, 3.5, 3.5]
y_u = [2, 1.5, 1.5, 2 ]

# Coordenadas para la letra "s"
x_s = [5, 4.5, 4.5, 5, 5, 4.5]
y_s = [2, 2, 1.8, 1.8, 1.5, 1.5]

# Crear la figura y el gráfico
fig, ax = plt.subplots()

# Graficar 
ax.plot(x_l, y_l, marker='o', linestyle='-')
ax.plot(x_a, y_a, marker='o', linestyle='-')
ax.plot(x_m, y_m, marker='o', linestyle='-')
ax.plot(x_u, y_u, marker='o', linestyle='-')
ax.plot(x_s, y_s, marker='o', linestyle='-')

# Etiquetar los puntos"l"
for i, (xi, yi) in enumerate(zip(x_l, y_l)):
    ax.annotate(f'({xi},{yi})', (xi, yi), textcoords="offset points", xytext=(0,5), ha='center')

# Etiquetar los puntos"a"
for i, (xi, yi) in enumerate(zip(x_a, y_a)):
    ax.annotate(f'({xi},{yi})', (xi, yi), textcoords="offset points", xytext=(0,5), ha='center')

# Etiquetar los puntos"m"
for i, (xi, yi) in enumerate(zip(x_m, y_m)):
    ax.annotate(f'({xi},{yi})', (xi, yi), textcoords="offset points", xytext=(0,5), ha='center')

# Etiquetar los puntos"u"
for i, (xi, yi) in enumerate(zip(x_u, y_u)):
    ax.annotate(f'({xi},{yi})', (xi, yi), textcoords="offset points", xytext=(0,5), ha='center')

# Etiquetar los puntos"s"
for i, (xi, yi) in enumerate(zip(x_s, y_s)):
    ax.annotate(f'({xi},{yi})', (xi, yi), textcoords="offset points", xytext=(0,5), ha='center')


# Mostrar el gráfico 
plt.xlabel('Coordenada X')
plt.ylabel('Coordenada Y')
plt.title('Letra "e" con Coordenadas')
plt.grid(True)
plt.show()

#Siguiente nombre 
----------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt

# Coordenadas para la letra "e"
x_e = [0.5, 0, 0, 0.5, 0, 0, 0.5]
y_e = [2.5, 2.5, 1.5, 1.5, 1.5, 2, 2]

# Coordenadas para la letra "d"
x_d = [1.5, 1.5, 1, 1, 1.5]
y_d = [2.5, 1.5, 1.5, 2, 2 ]

# Coordenadas para la letra "g"
x_g = [2, 2.5, 2.5, 2, 2, 2.5]
y_g = [1, 1, 2, 2, 1.5, 1.5 ]

# Coordenadas para la letra "a"
x_a = [3.5, 3, 3, 3.5, 3.5]
y_a = [1.5, 1.5, 2, 2, 1.4 ]

# Coordenadas para la letra "r"
x_r = [4.2, 4, 4]
y_r = [2, 2, 1.5]

# Crear la figura y el gráfico
fig, ax = plt.subplots()

# Graficar la letra "e"
ax.plot(x_e, y_e, marker='o', linestyle='-')
ax.plot(x_d, y_d, marker='o', linestyle='-')
ax.plot(x_g, y_g, marker='o', linestyle='-')
ax.plot(x_a, y_a, marker='o', linestyle='-')
ax.plot(x_r, y_r, marker='o', linestyle='-')

# Etiquetar los puntos"e"
for i, (xi, yi) in enumerate(zip(x_e, y_e)):
    ax.annotate(f'({xi},{yi})', (xi, yi), textcoords="offset points", xytext=(0,5), ha='center')

# Etiquetar los puntos"d"
for i, (xi, yi) in enumerate(zip(x_d, y_d)):
    ax.annotate(f'({xi},{yi})', (xi, yi), textcoords="offset points", xytext=(0,5), ha='center')

# Etiquetar los puntos"g"
for i, (xi, yi) in enumerate(zip(x_g, y_g)):
    ax.annotate(f'({xi},{yi})', (xi, yi), textcoords="offset points", xytext=(0,5), ha='center')

# Etiquetar los puntos"a"
for i, (xi, yi) in enumerate(zip(x_a, y_a)):
    ax.annotate(f'({xi},{yi})', (xi, yi), textcoords="offset points", xytext=(0,5), ha='center')

# Etiquetar los puntos"r"
for i, (xi, yi) in enumerate(zip(x_r, y_r)):
    ax.annotate(f'({xi},{yi})', (xi, yi), textcoords="offset points", xytext=(0,5), ha='center')
# Mostrar el gráfico 
plt.xlabel('Coordenada X')
plt.ylabel('Coordenada Y')
plt.title('Letra "e" con Coordenadas')
plt.grid(True)
plt.show()

#Siguiente nombre 
----------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt

# Coordenadas para la letra "d"
x_d = [0, 0, 0.5, 0.5, 0]
y_d = [1.5, 2.5, 2.25, 1.8, 1.5]

# Coordenadas para la letra "a"
x_a = [1.5, 1.5, 1, 1, 1.5]
y_a = [1.4, 2, 2, 1.5, 1.5 ]

# Coordenadas para la letra "n"
x_n = [2.5, 2.5, 2, 2]
y_n = [1.5, 2, 2, 1.5]

# Coordenadas para la letra "i"
x_i = [3, 3]
y_i = [1.5, 2]

# Coordenadas para la letra "e"
x_e = [3.5, 4, 4, 3.5, 3.5, 4]
y_e = [1.8, 1.8, 2, 2, 1.5, 1.5]

# Coordenadas para la letra "l"
x_l = [4.5, 4.5]
y_l = [1.5, 2.5]

# Crear la figura y el gráfico
fig, ax = plt.subplots()

# Graficar 
ax.plot(x_d, y_d, marker='o', linestyle='-')
ax.plot(x_a, y_a, marker='o', linestyle='-')
ax.plot(x_n, y_n, marker='o', linestyle='-')
ax.plot(x_i, y_i, marker='o', linestyle='-')
ax.plot(x_e, y_e, marker='o', linestyle='-')
ax.plot(x_l, y_l, marker='o', linestyle='-')

# Etiquetar los puntos"d"
for i, (xi, yi) in enumerate(zip(x_d, y_d)):
    ax.annotate(f'({xi},{yi})', (xi, yi), textcoords="offset points", xytext=(0,5), ha='center')

# Etiquetar los puntos"a"
for i, (xi, yi) in enumerate(zip(x_a, y_a)):
    ax.annotate(f'({xi},{yi})', (xi, yi), textcoords="offset points", xytext=(0,5), ha='center')

# Etiquetar los puntos"n"
for i, (xi, yi) in enumerate(zip(x_n, y_n)):
    ax.annotate(f'({xi},{yi})', (xi, yi), textcoords="offset points", xytext=(0,5), ha='center')

# Etiquetar los puntos"i"
for i, (xi, yi) in enumerate(zip(x_i, y_i)):
    ax.annotate(f'({xi},{yi})', (xi, yi), textcoords="offset points", xytext=(0,5), ha='center')

# Etiquetar los puntos"e"
for i, (xi, yi) in enumerate(zip(x_e, y_e)):
    ax.annotate(f'({xi},{yi})', (xi, yi), textcoords="offset points", xytext=(0,5), ha='center')

# Etiquetar los puntos"l"
for i, (xi, yi) in enumerate(zip(x_l, y_l)):
    ax.annotate(f'({xi},{yi})', (xi, yi), textcoords="offset points", xytext=(0,5), ha='center')

# Mostrar el gráfico 
plt.xlabel('Coordenada X')
plt.ylabel('Coordenada Y')
plt.title('Letra "e" con Coordenadas')
plt.grid(True)
plt.show()
