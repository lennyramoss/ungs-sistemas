"""Escribir una función llamada maximo que tome una lista de números y devuelva el valor del
máximo elemento"""

def maximo(lista):
    mayor=0
    for numero in lista:
        if numero>mayor:
            mayor=numero
    return mayor


valores=[5,1,15,2]
numMayor=maximo(valores)
print(numMayor)