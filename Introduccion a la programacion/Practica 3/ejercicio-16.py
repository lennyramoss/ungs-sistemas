n = int(input("Ingrese la cantidad de terminos que desea usar "))
signo = 1
veces = 1
denom = n - 1
termino = 0
cont = 0


for i in range (1,n):
    if n % 2 == 0 :
        veces = veces*(-1)
    else:
        veces = veces
    termino = (veces)*(n + denom) 
    cont = cont + termino
print(termino)



"""for i in range(1,n):
    vece
    denom = signo+2  
    signo *= denom
    pi = 1/signo
    signo = -1
    veces+=1
print(pi)
"""

#la funcion modulo se pone como abs