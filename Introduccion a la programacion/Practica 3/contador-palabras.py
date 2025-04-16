palabra = input("Ingrese una palabra ")
cont = 0
for letra in palabra:
    cont+=1
    if cont == 1 or cont == 3:
        print(letra)