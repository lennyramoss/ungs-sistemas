"""¾Es verdad que las únicas soluciones de x(x+2)(x+3) = 1 son x = 1 x = −2 y x = −3?. 
Hacer un programa que encuentre to das las soluciones de 1 0 2 cifras tanto negativas como 
positivas."""


x = -99

while x<=99:
    resultado = x ** ((x + 2) * (x + 3))
    if resultado == 1:
        print(x)
    x+=1