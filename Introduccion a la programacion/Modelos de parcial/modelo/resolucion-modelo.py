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

"""4  8 comisiones en 3 turnos 
el estudiantes debe elegir el turno y si hay vacante se le asigna una comision de ese turno
a) Hacer una función que reciba el turno deseado y las listas con la información de las comisiones, si hay 
vacante deberá descontarla de la lista de cantidad de alumnos  disponibles de esa comisión y devolver la 
comisión asignada. SI no hay ninguna vacante disponible, deberá devolver 0."""
def checkTurno(turnosSolicitado,turnos,cantidad):
    for i in range(len(cantidad)):
        if turnosSolicitado == turnos[i]:
            if cantidad[i]-1>0:
                cantidad[i]=cantidad[i]-1 #IMPORTANTE COMO SE RESTA A UN VALOR X DE LA LISTA
                return cantidad
            return 0
              


ComisionesHabilitadas=[1,2,3,4,5,6,7,8]
TurnoDeCadaComision  =["M","T","N","M","N","T","N","M"]
CantidadAlumPorComision=  [80,80,60,50,40,50,50,40]
pedidoTurno= str(input("Elegi entre turno mañana,tarde,noche: ")).upper()

print (checkTurno(pedidoTurno,TurnoDeCadaComision,CantidadAlumPorComision))

#b) Realizar el programa principal que cuenta con una lista de DNIs y otra con los turnos elegidos e imprime 
#en pantalla DNI y comisión asignada o DNI y sin vacante. 
listaDni=[]
listaTurnoDeseado=[]
cant=int(input("ingrese la cantidad personas que desea anotar "))
i=1
while cant>=i:
    dni=int(input("Ingrese el DNI "))
    comision=str(input("Ingrese la comision que desea el dni(m,t,n) ")).upper()
    listaDni.append(dni)
    listaTurnoDeseado.append(comision)
    i+=1

for i in range(len(listaDni)):
    if listaTurnoDeseado[i] == TurnoDeCadaComision[i]:
        if CantidadAlumPorComision[i]-1>0:
            CantidadAlumPorComision[i]=CantidadAlumPorComision[i]-1 #IMPORTANTE COMO SE RESTA A UN VALOR X DE LA LISTA
            print(listaDni[i],ComisionesHabilitadas[i])
    else:
        print("no hay mas comisiones disponibles")
        
