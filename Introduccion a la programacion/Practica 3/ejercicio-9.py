"""
 a) Hacer un programa que reciba un número n y muestre todas las potencias de 2
 menores a n. Por ejemplo, si el usuario ingresa 20, el programa mostrará: 1 2 4 8
 16. Ayuda: pensar primero si sería más práctico utilizar la sentencia while o for.
 b) Hacer un programa que reciba un número n (n > 0) y muestre las n primeras
 potencias de 2. Por ejemplo, si el usuario ingresa 6, el programa mostrará: 1 2 4 8
 16 32.
 c) Hacer un programa que reciba un número n (n > 0) y muestre las n primeras
 potencias de n. Por ejemplo, si el usuario ingresa 4, el programa mostrará: 1 4 27
 256. Es decir, 11 22 33 44."""



#a)
n = int(input("Ingrese el numero n "))
i = 2
resultado = 2

while resultado<n:
    print(resultado)
    resultado = 2**i
    i+=1


#b)
n = int(input("Ingrese la cantidad de veces que desea elevar a 2 "))
i = 1
resultado = 2

while i<=n:
    print(resultado)
    resultado = 2**i
    i+=1

#c)

n = int(input("Ingrese el numero n "))
i = 1
resultado = 0

while i<=n:
    resultado = i**i
    print(resultado)
    i+=1