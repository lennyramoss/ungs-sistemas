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



#EJERCICIO 2
def palabraRand(palabra):
    letras=[]
    letrasRandom=""
    for letra in palabra:
        letras.append(letra)
    for i in range(2):
        numRandom= random.randint(0,len(palabra)-1)
        letrasRandom+=letras[numRandom]
    return palabra + letrasRandom


print(palabraRand("veterinario"))

#b
def palabraRandRepetido(palabra):
    letras=[]
    letrasRandom=""
    for letra in palabra:
        letras.append(letra)
    for i in range(2):
        numRandom= random.randint(0,len(palabra)-1)
        if numRandom==numRandom:
            numRandom-=1
        letrasRandom+=letras[numRandom]
    return palabra + letrasRandom


print(palabraRandRepetido("pero"))

#EJERCICIO 3
