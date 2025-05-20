"""a) Definir una función que tome una lista de números s y un número decimal x y
devuelva la cantidad de elementos de s que sean menores que x.
b) Si se pone como condición que s siempre esté ordenada de mayor a menor, ¾cómo
podría modifocarse el programa para que haga menos iteraciones"""

def qwe(lista,x):
    for numero in lista:
        if numero<x:
            #listaNueva.append(numero)
            print(numero)

numerosS=[25,87,147,67,24,7,12,6]

qwe(numerosS,54)


