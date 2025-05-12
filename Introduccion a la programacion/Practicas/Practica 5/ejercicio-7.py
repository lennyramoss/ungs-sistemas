def dondeAparece(lista,blanco):
    for i in range(len(enteros)):
        if lista[i] == blanco:
            return i
    return -1
    



enteros=[1,2,3,4]
num = int(input("Ingrese un valor "))
print(dondeAparece(enteros,num))


"""NO USAR APPEND Y POP EN LOS CICLOS for SEGUNDO EJEMPLO
LAS CADENAS SON INMUTABLES Y LAS CADENAS SON MUTABLES
PRACTICAR LISTAS"""