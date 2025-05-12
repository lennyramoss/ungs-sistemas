def sonFactores(n,lista):
    contador=0
    for divisores in lista:
        calc=n%divisores
        if calc==0:
            contador+=1
    if len(lista)==contador:
        return True
    else:
        return False 




n = int(input("Ingrese un numero "))
enteros = [1,2,3,4,5]
if sonFactores(n,enteros):
    print(f"Es divisible por estos valores:{enteros}")
else:
    print(f"No es divisibles por estos valores:{enteros}")
