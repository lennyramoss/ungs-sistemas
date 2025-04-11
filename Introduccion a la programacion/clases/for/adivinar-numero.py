import random
a= random.randint(1,100)
vidas =  3
print("Adivina el numero del 1 al 100")
print (a)
intentos = 1
while vidas>=intentos:
    dato = int(input("ADIVINA EL NUMERO: "))
    if a==dato:
        print("adivinaste")
    else:
        print("No adivinaste")
    intentos+=1



#como salgo del if cuando acerto??? (break no)