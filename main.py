from random import randint

def getWord():
    with open("./Data/palabras.txt","r") as f:                
        a = [i for i in f]
    return a.pop(randint(0, len(a)-1)).replace("\n", "")


def getSyllable():
    while True:
        sil = input("Ingrese la letra: ").upper()
        if sil.isalpha():
            break        
        else:
            print("Ingrese un valor del alfabeto")
    return sil


def run():
    points = 0
    wordInGame = "ELPEPE"
    wordInGameList = [i for i in wordInGame]    
    wordInGameUnderscore = ["___" for i in wordInGame]

    

if __name__=='__main__':
    run()
