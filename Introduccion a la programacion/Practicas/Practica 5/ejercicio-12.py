"""Escribir una función llamada intercambiar que tome una lista de números s y dos enteros
positivos a y b menores que la longitud de la lista y cambie el elemento ubicado en s[a] p or el
elemento ubicado en s[b]. Ojo, esta función no deb e devolver una lista, sino modificar la que
toma como parámetro."""


def intercambiar(lista,a,b):
    if a<len(lista)>b:
        aux=lista[b]
        lista[b] = lista[a]
        lista[a] = aux
        print(f"la lista modificada {lista}")
    else:
        print("los valores a y b no estan dentro de la lista")

numeros=[0,7,5,4,1,12]
n1=int(input("Ingrese un numero "))
n2=int(input("Ingrese otro numero "))

intercambiar(numeros,n1,n2)



#if lista[i] > lista[indice_max]