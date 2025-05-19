"""Escribir una función llamada maximoEntre que tome una lista de números y dos enteros a y b
menores que la longitud de la lista y devuelva el índice del máximo elemento considerando solo
los que están entre el índice a y el índice b."""

def maximoEntre(lista,a,b):
    mayor=0
    if a>0 and b<len(lista)-1:
        return False
    for i in range(a,b):
        if lista[i]>mayor:
            mayor=lista[i]
    return mayor


        

numeros = [1,2,3,4,5,6]
print(numeros)
n1=int(input(f"Ingrese un numero "))
n2=int(input("Ingrese otro numero "))
maxAYB=maximoEntre(numeros,n1,n2)
print(f"el mayor valor entre el {n1} y {n2} es {maxAYB}")