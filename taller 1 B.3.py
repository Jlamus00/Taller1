print("Ingrese el numero de la figura")
print("1. Prisma")
print("2. Piramide")
print("3. Cono truncado")
f= input("4. Cilindro \n")


if(int(f)==1):
    largo=input("Ingrese lo largo del prisma: (cm)\n")
    ancho=input("Ingrese el ancho del prisma: (cm)\n")
    altura=input("Ingrese la altura del prisma: (cm)\n")

    V=int(largo)*int(ancho)*int(altura)

    print('El volumen del prisma es  '+str(V)+'cm^3')

elif(int(f)==2):
    base=input("Ingrese lo base del piramide: (cm)\n")
    altura=input("Ingrese la altura del piramide: (cm)\n")

    V=(int(base)*int(altura))/3

    print('El volumen del piramide es  '+str(V)+'cm^3')

elif(int(f)==3):
    R=input("Ingrese lo radio de la base mayor del cono truncado: (cm)\n")
    r=input("Ingrese lo radio de la base menor del cono truncado: (cm)\n")
    altura=input("Ingrese la altura del cono truncado: (cm)\n")

    V=(1/3)*float(3.14159)*(int(R)**2+int(r)**2+int(R)*int(r))*int(altura)

    print('El volumen del cono truncado es  '+str(V)+'cm^3')

elif(int(f)==4):
    r=input("Ingrese lo radio del Cilindro: (cm)\n")
    altura=input("Ingrese la altura del Cilindro: (cm)\n")

    V=(float(3.14159)*int(r)**2)*int(altura)

    print('El volumen del cilindro es  '+str(V)+'cm^3')

else:
    print('Numero invalido  ')


