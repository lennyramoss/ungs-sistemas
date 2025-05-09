cons = ["b","c","d","f","g","h","j","k","l","m","n","ñ","p","q","r","s","t","v","w","x","y","z"]
import random


def buscar_consonantes(apellido.lower()):
    cont = 0
    for letra in apellido:
        if cons in apellido and cont<4:#no es igual a 4 porque el cont arranca en 0
            apcons +=cons
            cont+=1
    return apcons

def crear_clave(apellido):
    if len(apcons) == 4:
        clave = apcons+str(randint(0,9))
    elif len(apcons) == 3:
        clave = apcons+"*"+str(randint(0,9))
    elif len(apcons) == 2:
        clave = apcons+"**"+str(randint(0,9))
    elif len(apcons) == 1:
        clave = apcons+"***"+str(randint(0,9))
    else:
        clave = "****"+str(randint(0,9))
    """
    apcons=clave
    while (len(apcons))<4
        clave += ""*"""
        

ape = input("ingrese su apellido")
print(crear_clave(ape))



