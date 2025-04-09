import random
n = random.randrange(1,101)
i=0
x = 0
for i in range(1,4):
    if x==n:
        x  = int(input("Adivine el numero"))
    else:
        print("No adivinaste")