"""Definir una función que tome un entero n y devuelva los primeros n primos."""

def primos(a):
    nPrimos=[]
    while len(nPrimos)<a:
        for i in range(2,a*5):
            cont=0
            for j in range(1,i+1):
                if i%j==0:
                    cont+=1
            if cont==2:
                nPrimos.append(i)
             
            
primos(5)

"""def primos(a):
    nPrimos = []
    num = 2  # empezamos desde el primer número primo
    while len(nPrimos) < a:
        cont = 0
        for j in range(1, num + 1):
            if num % j == 0:
                cont += 1
        if cont == 2:
            nPrimos.append(num)
        num += 1
    return nPrimos

print(primos(5))  # [2, 3, 5, 7, 11]
"""