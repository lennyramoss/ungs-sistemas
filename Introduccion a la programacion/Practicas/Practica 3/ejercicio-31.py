"""
Hacer un programa que solicite dos cadenas, nombre y ap ellido y arme el lega jo de estudiantes
de la universidad de la siguiente manera:
Los 3 primeros números del lega jo coinciden con los primeros del dni luego "_", luego las 3
primeras letras del ap ellido y p or ultimo la primera y ultima del nombre.
Por ejemplo:
JavierRodriguez 38946702
Lega jo: 389_rodjr
"""

nombre = str(input("Ingrese su nombre "))
apellido = str(input("Ingrese su apellido "))
dni = str(input("Ingrese su DNI "))
usuario=""
usuariodni=""
cont=0
long=0

for char in dni:
    cont+=1
    if cont<=3: #lo hace hasta que cont sea igual q 3
        usuariodni+=char
cont=0
for char in apellido:
    cont+=1
    if cont<=3:
        usuario+=char
for char in nombre:
    long+=1

cont=0
for char in nombre:
    cont+=1
    if cont==1 or cont==long:
        usuario+=char

print (f"{usuariodni}_{usuario}")