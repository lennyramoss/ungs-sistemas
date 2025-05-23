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

def repetida(palabra)
    palabraDesarmada=[]
    for letra in palabra:
        if letra in palabraDesarmada:
            conteo[letra]+=1
        else:
            conteo[letra]
            palabraDesarmada.append(char)
