"""Definir una función llamada union que tome dos listas sin rep etidos y devuelva una nueva lista
que contenga los elementos de ambas listas. Ojo, la lista de retorno debe no tener rep etidos."""

def union(lista1,lista2,listaNueva):
    for numero1 in lista1:
        if numero1 not in lista2:
            listaNueva.append(numero1)
    for numero2 in lista2:
        if numero2 not in lista1:
            listaNueva.append(numero2)
    return listaNueva


valores=[0,2,5,12,56]
numeros=[0,12,22,56]
listaNueva=[]
unionListas=union(valores,numeros,listaNueva)
print(unionListas)                