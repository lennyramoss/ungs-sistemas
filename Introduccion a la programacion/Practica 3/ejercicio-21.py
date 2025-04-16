import random

n_ganador = random.randint(0,100)
monto = int(input("Ingrese el monto que desea jugar "))
n = int(input("Elija el numero del 1 al 100 "))
if n==n_ganador:
    monto*=70
    print("GANASTE",monto,"!!!!")
else:
    print("Perdiste,el número ganador fue el", n_ganador)