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