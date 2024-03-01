
print('(1) Cilindro')
print('(2) Carterciano')
print('(3) Esferica')
robot =input('Seleccione el robot que desea conocer:\n')

if  robot == '1':
    print ("Elegiste cilindrico: ")
    print("Este robot posee tres articulaciones una rotacional y dos prismaticas")
elif robot == '2':
    print("Elejiste cartesiano: ")
    print("Este robot posee tres articulaciones prismaticas")
elif robot == '3' :
    print ("Elegiste esferico:")
    print( "Este robot posee tres articulaciones dos rotacionales y una prismatica")
else :
    
    print("No es una de la opciones")