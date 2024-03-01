

import numpy as np
import matplotlib.pyplot as plt

def carga_descarga_RC(V, C, R, tiempo):

    tau = R * C  # Constante de tiempo RC
    carga = V * (1 - np.exp(-tiempo / tau))  # Ecuación de carga
    descarga = V * np.exp(-tiempo / tau)  # Ecuación de descarga
    return carga, descarga

def graficar_carga_descarga(tiempo, carga, descarga):
    """
    Grafica la carga y descarga en un circuito RC.
    
    Parámetros:
    - tiempo: Array de tiempo
    - carga: Voltajes durante la carga
    - descarga: Voltajes durante la descarga
    """
    plt.figure(figsize=(10, 6))
    plt.plot(tiempo, carga, label='Carga')
    plt.plot(tiempo, descarga, label='Descarga', linestyle='--')
    plt.title('Carga y Descarga en un Circuito RC')
    plt.xlabel('Tiempo (segundos)')
    plt.ylabel('Voltaje (voltios)')
    plt.legend()
    plt.grid(True)
    plt.show()

# Obtener entrada del usuario
V = float(input("Ingrese el voltaje inicial (V): "))
C = float(input("Ingrese la capacitancia (μF): "))
R = float(input("Ingrese la resistencia (Ω): "))
tiempo = np.linspace(0, 5 * R * C, 1000)  # 5 veces la constante de tiempo para asegurar que alcance el estado estable

# Calcular carga y descarga
carga, descarga = carga_descarga_RC(V, C, R, tiempo)

# Graficar
graficar_carga_descarga(tiempo, carga,descarga)