import random as rdn
def word():
    with open("./DATA.txt","r") as f:                
        a = [i.replace("\n", "") for i in f]
    return a.pop(rnd.randint(0, len(a)-1))

def run():
    puntos = 0
    palabraEnJuego = word()
    while True:
        menu(word())
        letra = input("Ingrese la letra a buscar")


if __name__=='__main__':
    run()
