#Interfaz

resp = input('¿Desea iniciar?(y/n): ').capitalize()
assert resp == 'Y' or resp == 'N', 'Ingrese solo y o n'
if resp == 'N':
    print('El programa finalizó, gracias por su visita')
else:
    print(30*'*'+'BIENVENIDO'+'*'*30)