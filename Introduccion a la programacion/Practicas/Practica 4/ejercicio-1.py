def raiz(n):
    for i in range(1,n):
        calc= i**2
        if calc==n:
            return calc

def modulo(n):
    if n<0:
        calc=n+(n*-2)
        return calc
    return n

def moduloMenosTres(n):
    if n<3:
        calc=(n-3)*-2
    else:
        calc=n-3
    return calc
 
def raizYModuloMenosCinco(n):
    mod=0
    if n<5:
        mod=(n-5)*-2
    elif n==5:
        print("no existe la raiz de 0")
        return n
    else:
        mod=n-5
    for i in range(1,mod):
        raizModulo= i**2
        if raizModulo==mod:
            return i
    print("No se encontró una raíz cuadrada exacta")
    return None



raizN=raiz(16)
moduloN=modulo(-4)
modMenosTres=moduloMenosTres(-4)
raizMod=raizYModuloMenosCinco(7)
print(raizN,moduloN,modMenosTres,raizMod)