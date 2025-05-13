"""Escribir una función llamada maximoIndice que tome una lista de números y devuelva el
índice del máximo elemento"""

def maximoIndice(lista):
    indice_max = 0  
    for i in range(1, len(lista)):
        if lista[i] > lista[indice_max]: #if valores=5 >
            indice_max = i  # Si encontramos uno mayor, actualizamos el índice
    return indice_max

    
valores=[5,1,3,4,9,15,2]
maxInd=maximoIndice(valores)
print(maxInd)
