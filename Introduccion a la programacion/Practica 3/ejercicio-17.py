e = int(input("Ingrese la cantidad de terminos que desea usar "))
suma=0
div=0

for i in range (e):
    div = 1/i
    suma += div
print(suma)