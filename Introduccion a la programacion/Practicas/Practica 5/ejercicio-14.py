"""Definir una función llamada interseccion que tome dos listas sin rep etidos y devuelva una
nueva lista que contenga sólamente aquellos elementos que estén ambas listas"""

def interseccion(lista1,lista2,lista3):
    for numero1 in lista1:
        for numero2 in lista2:
            if numero1 == numero2:
                lista3.append(numero1)
    return lista3


primerLista=[1,2,3,4,5]
segundaLista=[4,5,6,7,8]    
listaNueva=[]

repes=interseccion(primerLista,segundaLista,listaNueva)
print(repes)
