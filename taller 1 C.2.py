import numpy as np
import matplotlib.pyplot as plt


fn = float(input("Ingrese el frecuencia natural:\n "))
g = float(input("Ingrese la ganancia: \n "))
fa = float(input("Ingrese el factor de amortiguamiento \n "))
vari = [fn, g, fa]

def segundo_orden(s):
    pr = np.array([vari[0]])  
    pd = np.array(vari[1:])   
    return np.polyval(pr, s) / np.polyval(pd, s)

def amortiguado():
    amo = vari[1]**2 - 4*vari[0]*vari[2] 
    if amo < 0:
        return 'Sistema subamortiguado'
    elif amo == 0:
        return 'Sistema críticamente amortiguado'
    else:
        return 'Sistema sobreamortiguado'

def grafica():
    t = np.linspace(0, 30, 1000)
    s = 1j * t
    y = segundo_orden(s)
    plt.plot(t, np.real(y))
    plt.plot(t, np.imag(y))
    plt.xlabel('Tiempo')
    plt.ylabel('Respuesta')
    plt.title('Respuesta del sistema')
    plt.legend()
    plt.grid()
    plt.show()

print("Sistema:", amortiguado())
grafica()
