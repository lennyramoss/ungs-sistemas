import random
a= random.randint(1,100)
print("Adivina el numero del 1 al 100")
print (a)

while 100>=a:
    for i in range(3):
        dato = int(input("ADIVINA EL NUMERO: "))
        if a==dato:
            print("adivinaste")
        else:
            print("No adivinaste")
