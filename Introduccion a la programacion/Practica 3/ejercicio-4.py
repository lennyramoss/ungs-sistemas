"""a) Hacer un programa que muestre, mediante un ciclo, los números desde el 5 hasta el
11 salteando de a 2 elementos (5,7,9 y 11)
b) Hacer un programa que p ermita al usuario elegir un número m y un n y luego
muestre to dos los naturales entre m y n, p ero salteando de a 3. Por ejemplo, si el
usuario ingresara un n igual a 2 y un m igual a 14, el programa deb erá mostrar
2, 5, 8, 11, 14.
c) Hacer un programa que p ermita al usuario elegir un número n, un m y un p y
luego muestre to dos los naturales entre m y n, p ero salteando de a p números. Por
ejemplo, si el usuario ingresara un n igual a 2 y un m igual a 14, y un p igual a 4,
el programa deb erá mostrar 2, 6, 10, 14
"""

#a)
i = 5
while i<=11:
    print(i)
    i = i + 2


#b)
m = int(input("Ingrese el inicio del intervalo "))
n = int(input("Ingrese el fin del intervalo "))
i = 1
while m<=n:
    print(m)
    m+=3


#c)
m = int(input("Ingrese el inicio del intervalo "))
n = int(input("Ingrese el fin del intervalo "))
p = int(input("Ingrese de a cuantos quiere saltear "))
while m<=n:
    print(m)
    m+=p
    
