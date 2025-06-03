def coprimos(a,b):
    for i in range(2,a+1):
        if a%i==0 and b%i==0:
            return print("no son coprimos")
    return print("son coprimos")


coprimos(15,28)
coprimos(12,18)



def promCuatro(lista):
    promediados=[]
    for numero in lista:
        if numero>=4:
            promediados.append(numero)
    return promediados


valores=[]
cantNumeros= int(input("Ingrese la cantidad de valores que desea agregar "))
for i in range(cantNumeros):#NO USAR APPEND Y POP EN LOS CICLOS forSEGUNDO EJEMPLO
    numerosUsuario= float(input("Ingrese los valores que desea "))
    valores.append(numerosUsuario)

mayorQCuatro=promCuatro(valores)
print(f"estos valores son mayor o iguales que 4 {mayorQCuatro}")





abcd=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"] 



listaPalabra=[]
listaClave=[]
listaTextoOculto=[]
posicionPalabra=[]
posicionClave=[]
textoOculto=""
palabraEncriptada = str(input("Ingrese la palabra encriptada ")).upper()
claveUsuario = str(input("Ingrese la clave ")).upper()

for letra in palabraEncriptada:
    listaPalabra.append(letra)

for letra in claveUsuario:
    listaClave.append(letra)
#estas dos lineas desarman la palabra en letras

for letra in listaPalabra:
    for i in range(len(abcd)): # lo sumo aca porque no se le puede sumar uno a una lista de strings
        if letra == abcd[i]:
            posicionPalabra.append(i+1)

for letra in listaClave:
    for i in range(len(abcd)):
        if letra== abcd[i]:
            posicionClave.append(i+1)# lo sumo aca porque no se le puede sumar uno a una lista de strings
#lugar de cada letra de la palabra en abdc

if len(listaPalabra)>len(listaClave):
    for posicion in range(len(listaPalabra)):
        listaTextoOculto.append(posicionPalabra[posicion] - posicionClave[posicion])

else:
    for posicion in range(len(listaClave)):
        listaTextoOculto.append(posicionPalabra[posicion] - posicionClave[posicion])

for lugar in listaTextoOculto:
    for j in abcd:
        if lugar == abcd[j]:
            textoOculto+=abcd[j]



#4

for i in range(len(materias)):
    cont=0
    for preMateria in correlativas(materias[i]):
        if aprobada(dni[i],preMateria):
            cont+=1
        else:
            borrarLista.append(i)
        if cont==len(correlativas(materias[i])):
            if not controlaSuperposicion(dni[i],horario(preMateria)):
                borrarLista.append(i)

for numero in borrarLista:
    max=0
    for indice in borrarLista:
        if numero>indice:
            max=numero
        borrarListaOrdenada.append(max)

for indice in borrarListaOrdenadas:
    dni.pop(indice)
    materia.pop(indice)
            

