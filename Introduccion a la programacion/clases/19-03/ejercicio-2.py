a = int(input("Ingrese un valor "))
b = int(input("Ingrese otro valor "))
if a>0 and b>0:
    print("El resultado es positivo")
elif a<0 and b<0:
    print("El resultado es positivo")
elif a<0 and b>0:
    print("El resultado es negativo")
elif a>0 and b<0:
    print("El resultado es negativo")   
elif a==0 or b==0:
    print("Su resultado es 0")