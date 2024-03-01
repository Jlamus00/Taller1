# Se capturan los valores inciales para ingresar en la expresión
r= input("ingrese valor de resistencia: ")
i= input("Ingrese la la corriente: ")

r1=int(r)
i1=int(i)

v0=0
p0=0
#Calcular la expresión numérica para obtener la posición final
v0=(r1*i1)
p0=(v0*i1)

# Se convierten los valores a decimales
float(v0)
float(p0)
#Mostar el resultado final

print('resultado de voltaje '+str( v0) +' v')
print('resultado de potencia '+str( p0) +' A')