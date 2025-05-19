def elementoListaRepetido(primerLista,segundaLista):
    for i in range(0,len(primerLista)):
        for j in range(0,len(segundaLista)):
            if primerLista[i]==segundaLista[j]:
                return True
    return False



lista1 = [1,2,3,4]
lista2 = [5,6,7,8]
agregarNumero = int(input("Ingrese un numero "))
lista2.append(agregarNumero)

if elementoListaRepetido(lista1,lista2):
    print("Tiene elementos repetidos")
else:
    print("no tiene elementos repetidos")

