"""1. Máximo y su posición
Pedí al usuario una lista de números y mostrá cuál es el número más alto 
y en qué posición aparece por primera vez.

2. Promedio y comparación
Ingresá varios números y calculá el promedio. Mostrá cuántos números están por encima del promedio.

3. Vocales distintas
Pedí al usuario una palabra o frase y contá cuántas vocales diferentes contiene.
No debés contar repeticiones.

4. Palabra más larga
Ingresá varias palabras y mostrale al usuario cuál es la más larga de todas.
"""



#1
numeros=[1,7,4,2,3,5,7,6]
AltoNum=0
for numero in numeros:
    if numero>AltoNum:
        AltoNum=numero

for i in range(len(numeros)):
    if numeros[i] == AltoNum:# probar que pasa si pongo altonum in numeros
        print(i)


#2
def prom(notas,aprob):
    for nota in notas:
        if nota>=aprob:
            print("notas",nota)

notas=[6,3,6,7,8,3,2,4,2,1,1,1,1,2,5,10]
aprob=7
prom(notas,aprob)


#3

def contarVocales(texto):
    vocales=["a","e","i","o","u"]
    vocalesPalabra=[]
    textoSinEspacios = ""
    texto = texto.lower()

    for letra in texto:
        if letra != " ":#si la letra no es un espacio vacio
            textoSinEspacios += letra.lower()#se cumple
    print(textoSinEspacios)

    for letra in textoSinEspacios:
        if letra in vocales and letra not in vocalesPalabra:#agrega una sola vez la vocal
            vocalesPalabra.append(letra)

    for vocal in vocalesPalabra:#da cada vocal
        cont=0
        for letra in textoSinEspacios:#recorre cada letra del texto
            if letra==vocal:#pregunta si letra es igual a la VOCAL(INDIV) del for, esto lo que hace compara letra x letra si es igual a la vocal +1
                cont+=1
        print(vocal,cont)

contarVocales("EL AVION SE ESTRELLO")


#4 Ingresá varias palabras y mostrale al usuario cuál es la más larga de todas.
def long(lista):
    palabrasLongs=[]
    letrasMax=0

    for palabra in lista:
        cont=0
        for letra in palabra:
            cont+=1

        if cont>letrasMax:
            letrasMax=cont
            palabrasLongs = [palabra]# Acá reemplazamos completamente la lista de palabras largas

        elif cont==letrasMax:#si el cont actual es igual que la palabra con mas letras, lo agrega
            palabrasLongs.append(palabra)  # agrega si tiene igual largo
    print(palabrasLongs)


palabras=["avion","perro","terremoto","libro","cuaderno","maleta","computadora","indio"]
long(palabras)



#Escribí un programa que reciba una lista de palabras y muestre:
cant=int("ingrese la cantidad de palabras que va a ingresar ")
for i in range(len(cant)):
    palabras= str(input("Ingrese las palabras "))

for 