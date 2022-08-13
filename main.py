from random import randint
import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
    
def getWord():
    with open('./Data/palabras.txt','r') as f:                
        a = [i for i in f]
    return a.pop(randint(0, len(a)-1)).replace('\n', '')


def getSyllable():
    while True:
        sil = input('Ingrese la letra: ').upper()
        if sil.isalpha():
            break        
        else:
            print('Ingrese un valor del alfabeto')
    return sil

def printWord(wordList):
    for [i,j] in wordList:
        print(j, end=" ")
    print("\n")
    

def run():
    points: int = 100
    wordInGame = getWord()
    wordInGameList = [[i,j] for i,j in enumerate(wordInGame)]
    wordInGameUnderscore = [[i, '_'] for i in range(len(wordInGameList))]
    
    while wordInGameList != wordInGameUnderscore:
        printWord(wordInGameUnderscore)
        syl = getSyllable()
        
        for i in range(len(wordInGameList)):
            if wordInGame[i] == syl:
                wordInGameUnderscore[i] = [i,syl]
        points -= 1
        clearConsole()
    print(wordInGame)
    print("Ganaste capo, me siento orgulloso")    
    print("Puntos: "+str(points))

if __name__=='__main__':
    run()
