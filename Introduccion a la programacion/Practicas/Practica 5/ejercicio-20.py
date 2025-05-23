"""a) Definir una función que tome una lista de números s y un número decimal x y
devuelva la cantidad de elementos de s que sean menores que x.
b) Si se pone como condición que s siempre esté ordenada de mayor a menor, ¾cómo
podría modifocarse el programa para que haga menos iteraciones"""

#a


def menorX(lista,x):
    cont=0
    for numero in lista:
        if numero<x:
            cont+=1
    print(cont)

numerosS=[25,87,147,67,24,7,12,6]

menorX(numerosS,20)


def menorK(lista,x):
    for i in range(len(lista)):
        if lista[i]<x:
            return len(lista)-i#al estar ordenada resta el tamaño de la lista - el indice del que deja de ser mayor q x
    return False #si ninguno es menor que x

numerosK=[147, 87, 67, 25, 24, 12, 7, 6]

menorMejorado=menorK(numerosK,67)
print(menorMejorado)