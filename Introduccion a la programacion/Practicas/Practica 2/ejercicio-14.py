a = int(input("Ingrese el primer valor "))
b = int(input("Ingrese el segundo valor "))

if a<b:
    c=a
    a=b
    b=c
print("Los valores en orden de mayor a menor:", a, ",", b)