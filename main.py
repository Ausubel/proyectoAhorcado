import random as rdn
def word():
    with open("./DATA.txt","r") as f:                
        a = [i.replace("\n", "") for i in f]
    return a.pop(rnd.randint(0, len(a)-1))

def run():
    resp = input('¿Desea iniciar?(y/n): ').capitalize()
    assert resp == 'Y' or resp == 'N', 'Ingrese solo y o n'
    if resp == 'N':
        print('El programa finalizó, gracias por su visita')
    else:
        print(30*'*'+'BIENVENIDO'+'*'*30)    


if __name__=='__main__':
    run()
