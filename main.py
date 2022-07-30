from random import randint
def getWord():
    with open("./Data/palabras.txt","r") as f:                
        a = [i for i in f]
    return a.pop(randint(0, len(a)-1)).replace("\n", "")

def run():
    points = 0
    wordInGame = "ISABOTH"
    wordInGameList = [i for i in wordInGame]
    wordInGameUnderscore = str("___ "*len(wordInGame)) 

    lock = True
    letras = []
    while True:
        aux = input("Ingrese la letra: ")
        letras.append(aux)
        if aux.isalpha():
            break        
        else:
            print("Ingrese un valor del alfabeto")
    for i in wordInGameList:        
        print(wordInGameList.index(i))
        print(i,end=" ")
    

    




if __name__=='__main__':
    run()
