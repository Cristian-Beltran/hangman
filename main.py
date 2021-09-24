from random import randrange
import os




def Clear():
    """Funcion de limpieza de pantalla"""
    os.system("clear")



def Hello():
    """Mensaje de Bienvenida al juego"""
    print("Bienvenido al juego del ahorcado")
    print("Presiona Enter para comenzar con el juego")
    print("Si quieres salir presionsa Ctrl + c ")
    input()

def Game():
    """Inicio de valores de juego"""
    strikes = 0
    word = Random()
    res = []
    for i in range(1,len(word)+1): 
        res.append("_") 
    Play(strikes,res,word)

def Retry():
    x = input("Seguir jugando [S/N]")
    if x.lower() == 's':
        Game()
    else:
        print("Gracias por jugar hasta luego")
        exit()

def Win(word,res):
    string = ""
    for letter in res:
        string += letter 
    if word == string:
        print("Bien hecho acabas de ganar")
        Retry()


def lose():
    print("perdiste")
    Retry()


def String(res):
    """Contruccion de la palabra imprimida con espacios"""
    string = ""
    for i in range(0,len(res)):
       string += f" {res[i]} "  
    return string 


def Play(strikes,res,word):
    """Intentos de la partida"""
    Clear()
    print("Porfavor ingrese una letra")
    print(strikes)
    print(String(res))
    Win(word,res)
    letter = input(":").upper() #Ingreso de letra 
    if letter in word:
        for i in range(0,len(word)):
            if word[i] == letter:
                res[i] = letter
    else:
        if strikes >= 7:
            lose()
        else:
            strikes += 1

    Play(strikes,res,word) 


     


def Random():
    """Obtiene la lista de datos y selecciona de manera random"""
    DATA = Read()
    num = randrange(len(DATA))
    return DATA[num].upper()

def Read():
    """Lee los datos en el archivo data.txt y crea una lista"""
    DATA = []
    with open('./archivos/data.txt','r',encoding='utf-8') as r:
        DATA = [x[:-1] for x in r]
    return DATA


def Run():
    """Funcion de arranque"""
    try:
        Hello()
        Game()
    except KeyboardInterrupt:
        print("Gracias por jugar hasta luego")

if __name__=='__main__':
    Run()
