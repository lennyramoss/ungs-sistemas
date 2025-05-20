"""Definir una función llamada mcd que tome dos enteros p ositivos y devuelva el máximo común
divisor usando funciones de los ejercicios anteriores"""

def mcd (a,b,listaA,listaB,listaDivisores):
    i=1
    while i<=a:
        if a%i==0:
            listaA.append(i)
        i+=1
    i=1
    while i<=b:
        if b%i==0:
            listaB.append(i)
        i+=1
    for divisor in listaA:
        if divisor in listaB:
            listaDivisores.append(divisor)
    return listaDivisores[-1]



divN1=[]
divN2=[]
divisoresNumeros=[]
maxCD=mcd(24,32,divN1,divN2,divisoresNumeros)
print(maxCD)



