#1 
def palindromo(a):
    a = str(a)
    alreves=""
    for char in a:
        alreves= char + alreves
    if a==alreves:
        return True
    else:
        return False
    
print(palindromo(1578751))


#2

import random
def loteria(listaA,listaB,ganador,valor):
    ganadores=[]
    premio=0
    premioTotal=0
    total=0

    for i in range(0,len(listaA)):
        if listaA[i]==ganador:
            ganadores.append(i)
    if len(ganadores)==0:
        print("nadie gano ")
    elif len(ganadores)==1:
        premio = (listaB[ganadores[0]]*valor)*1.10
        print(f"El apostador {ganadores[0]+1} ganó {premio:.2f}$")
        premioTotal += premio
    else:
        for numero in ganadores:
            print(f"El apostador {numero+1} ganó ${listaB[numero]*valor}$") 
            premioTotal += listaB[numero]*valor

    for j in range(len(listaB)):
        total+=listaB[j]
    if total>premioTotal:
        print(f"las ganancias de este quinela son {total-premioTotal:.2f}$")
    elif total==premioTotal:
        print("este mes no hubo ganancia ")
    else:
        print(f"las perdidas de esta quienela son {total-premioTotal:.2f}$")


jugadores=[2,15,5,89,2,91,98,89,2,9]
apostado=[2,2.5,0.5,3,12,5,4.5,5,2.5,3]
bonus= int(input("Por cuanto se multiplicara el premio "))
nroGanador=int(input("Ingrese el nmumero ganador "))
loteria(jugadores,apostado,nroGanador,bonus)

"""while True:
jugador = int(input("Ingrese el numero que desea jugar "))
anotados.append(jugador)"""


#3
#from funciones import cadenaC

def repetida(c):
    c = c.lower()
    palabraDesarmada=[]#para guardas las letras unicas que aparecen la cadena
    repeticiones=[]#para guardas cuantas veces se repite cada letra 

    for letra in c:#recorre cada lentra en la palabra
        if letra not in palabraDesarmada:#si la letra no esta en la lista palabraDesarmada
            palabraDesarmada.append(letra)#la agrega
            contador=0#inicia un contador
            for otra in c: #recorre nuevamente la palabra 
                if letra == otra: #suma 1 al contador cada vez que encuentra esa letra
                    contador+=1 #agrega la cant de repeticiones a la lista de repeticiones
            repeticiones.append(contador)
            

    mayor=repeticiones[0]#es el mayor valor de apariciones encontrado hasta ahora, el 0 es porque iniciar con el primero
    pos_mayor=0#es la posición (índice) de esa cantidad en la lista
    for i in range (1,len(repeticiones)):#recoore el resta de la lista cantidades
        if repeticiones[i]>mayor:
            mayor=repeticiones[i]
            pos_mayor=i
            
    letra_mas_repetida=palabraDesarmada[pos_mayor]#obtiene la letra mas repetida usando su posicion dentro de la lista letras

    posiciones=[]
    for i in range(len(c)):#recorre la palabra
        if c[i]==letra_mas_repetida:#donde aparece la letra mas repetida
            posiciones.append(i)#le agrega i a la lista
    return posiciones
 
resultado = repetida("banana")
print(resultado)


#4
'''
~~ el animal haya comido y tomado, sino se le avisa al encargado
~~ se rellene el plato hasta 500g
~~ se rellene el agua hasta tener 5l
'''

if obtenerHora()=="07,00,00" or obtenerHora()=="16,00,00":
    for nroJaula in range(1,51):#cantidad jaulas
        comida=500-obtenerPesoAlimento(nroJaula)
        volcarAlimento(nroJaula,comida)

        agua=5-obtenerLitrosAgua(nroJaula)
        agregarAgua(nroJaula,agua)


elif obtenerHora()=="07,15,00" or obtenerHora()=="16,15,00":
    for nroJaula in range(1,51):#cantidad jaulas
        if obtenerPesoAlimento(nroJaula)<500 and obtenerLitrosAgua(nroJaula)<5:
            print(f"el perro de la jaula numero {nroJaula} comio ")#se puede hacer la cuenta para ver cuanta comida dejo
        elif obtenerPesoAlimento(nroJaula)==500 and obteneraLitrosAgua(nroJaula)==5:
            alertarEncargado(nroJaula)
