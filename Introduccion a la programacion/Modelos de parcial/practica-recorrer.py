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
notas=[6,3,6,7,8,3,2,4,2,1,1,1,1,2,5,10]
for nota in notas:
    if nota>=7:
        print("notas",nota)