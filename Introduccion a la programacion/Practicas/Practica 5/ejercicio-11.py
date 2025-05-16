"""Escribir una función llamada maximoEntre que tome una lista de números y dos enteros a y b
menores que la longitud de la lista y devuelva el índice del máximo elemento considerando solo
los que están entre el índice a y el índice b."""

def maximoEntre(lista,a,b):
    mayor=0
    if a<len(lista)>b: #if 0 <= a < len(lista) and 0 <= b < len(lista):
        for numero in range(a,b):
            if numero>mayor:
                mayor=numero
            return mayor
    else: 
        print("los valores a y b no estan dentro de la lista")




numeros = [0,1,2,3,4,5]
n1=int(input("Ingrese un numero "))
n2=int(input("Ingrese otro numero "))

maxAYB=maximoEntre(numeros,n1,n2)
print(f"el mayor valoe  entre el indice1 a y b es {maxAYB}")