"""Ejercicio 3 ⋆
a) Hacer un programa que muestre, mediante un ciclo, los 5 números naturales que le
siguen al 10 (11,12,··· ,15).
b) Hacer un programa que p ermita al usuario elegir un número n y luego muestre los
5 números naturales que le siguen a n (n + 1,n + 2,··· ,n + 5).
c) Hacer un programa que p ermita al usuario elegir un número n y un número c, y
luego muestre los c números naturales que le siguen a n (n + 1,n + 2,··· ,n + c).
"""


#a)
i=11

while i<=15:
    print(i)
    i += 1

#b)
n = int(input("Ingrese el primer valor "))
i = 0 #aclaro porque arriba tiene el valor de 11
i = n+5
while n<i:
    n +=1
    print(n)


#c)
n = int(input("Ingrese el primer valor "))
c = int(input("Ingrese el segundo valor "))
i = 1
while i<=c:
    print(n)
    n += 1
    i=i+1

