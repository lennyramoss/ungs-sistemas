"""armar un codigo que este formado por las 3 primeras letras
del apellido,las dos primeras y un numero aleatorio entre 0 y 99
el codigo deve estar en mayuscula"""

import random
nombre = input("Ingrese su nombre ")
apellido = input("Ingrese su apellido ")
usuario = ""
cont = 0

for letra in apellido:
    cont+=1
    if cont<=3:
        usuario += letra
cont=0
for letra in nombre:
    cont+=1
    if cont<=2:
        usuario += letra

numero = random.randint(0,99)
usuario = usuario.upper()
usuario = usuario + str(numero)
print(usuario)