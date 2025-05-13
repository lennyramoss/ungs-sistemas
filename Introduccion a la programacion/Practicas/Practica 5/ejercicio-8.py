"""Hacer una función que tome una lista de números decimales y devuelva el promedio de los
elementos"""


def promedio(lista):
    suma = 0
    for i in lista:
        suma += i
    nf=suma/len(lista)
    return nf
    #return round(nf, 2)   Devuelve el promedio con 2 decimales


notas = [7,7,6]
prom=promedio(notas)
print(prom)