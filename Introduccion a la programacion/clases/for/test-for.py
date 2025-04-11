for i in range(10):
    print("i=", i)



n = int(input("ingrese un número "))
acumulador = 0
for i in range (1,n+1): #Es n+1 porque asi incluye el valor, sino pararia antes (1 es inicio, n+1 es el fin)
    acumulador = acumulador + i
print ("la acumulacion de los",n,"primeros numeros es", acumulador)
