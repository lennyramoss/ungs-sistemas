import random
#EJERCICIO 1
"""for numero in range(100, 1000):  # Recorremos todos los números de 3 cifras
    str_num = str(numero)

    a = int(str_num[0])
    b = int(str_num[1])
    c = int(str_num[2])


    producto_digitos = a * b * c
    if numero == 4 * producto_digitos:
        print(f"El número es {numero}")
"""

for numero in range(100, 1000):
    a = numero // 100           # Centena
    b = (numero // 10) % 10     # Decena
    c = numero % 10             # Unidad


    if numero == 4 * a * b * c:
        print(f"El número es: {numero}")



"""2a Hacer una función que reciba una cadena y 
devuelva otra formada por dos elementos de esa cadena elegidos al azar."""

def caracRand(palabra):
    letras=[]
    palNew=""
    for letra in palabra:
        letras.append(letra)
    rand1=random.randint(0,len(letras)-1)
    rand2=random.randint(0,len(letras)-1)
    while letras[rand1]==letras[rand2]:
        rand2=random.randint(0,len(letras)-1)
    palNew=letras[rand1]+letras[rand2]
    print(palNew)

caracRand("perro")

#b) agregar a la función anterior que no pueda devolver el mismo caracter repetido.



"""Ejercicio 3: Hacer un programa que automatice la detección de patentes que se están buscando. El programa 
recibe una patente y un municipio donde buscar. Para ello cuenta con estas funciones: 
camaras(municipio): devuelve una lista de las cámaras del municipio. 
imagenes(camara): devuelve una lista con las patentes  que captó  la cámara. 
propietario(patente): devuelve a quien le pertenece el automotor con dicha patente. 
El programa debe devolver el nombre del propietario del automotor y la cámara donde se lo encontró o 
indicar que no se lo encontró en ese municipio."""

