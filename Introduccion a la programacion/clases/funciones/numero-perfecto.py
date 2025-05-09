def perfecto(n):
    total=0
    for i in range(1,n):
        if n%i == 0:
            total+=i
    if total==n:
        return True
    else:
        return False
    #cuando es si o no se utiliza booleanos


numero = int(input("Ingrese un numero "))
numero_perfecto = perfecto(numero)
if perfecto(numero):
    print(f"El numero {numero} es perfecto")
else:
    print(f"El numero {numero} no es perfecto")
