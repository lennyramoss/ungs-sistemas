"""a) Hacer un programa que p ermita al usuario elegir un número p ositivo n y luego
muestre en pantalla to dos los divisores de n.
b) Hacer un programa que p ermita al usuario elegir un número p ositivo n y luego
muestre en pantalla to dos los divisores pares de n.
c) Hacer un programa que p ermita al usuario elegir un número p ositivo n y luego
muestre en pantalla la cantidad de divisores de n.
d) Hacer un programa que p ermita al usuario elegir un número p ositivo n y luego
muestre en pantalla la suma de los divisores de n.
e) Hacer un programa que p ermita al usuario elegir dos números p ositivos c y n y luego
muestre en pantalla los primeros c divisores de n.
f ) Hacer un programa que p ermita al usuario elegir dos números p ositivos c y n y luego
muestre en pantalla los últimos c divisores de n"""



n = int(input("Ingrese un número para ver sus divisores "))
div_pos = 0
print("los divisores de",n,"son: ")
cant_div = 0
suma_div = 0
for i in range (1,n+1):
    div_pos = n%i
    if div_pos==0:
        cant_div +=1#c
        suma_div +=i#d
        print(i)#a
    
    if div_pos==0 and (i%2)==0:#b
        print("es divisor par",i)
  
print("la cantidad de divisores de",n,"es",cant_div)
print("la suma de los divisores de",n,"es",suma_div)


c = int(input("Ingrese el primer numero positivo "))
n = int(input("Ingrese el segundo numero positivo"))




