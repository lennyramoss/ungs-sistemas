def divisores(n):
    total=0
    for i in range(1,n+1):
        if n%i == 0 and i!=n:
            total+=i
    return total


numero = int(input("Ingrese un numero "))
sum_div = divisores(numero) # la guardo en la variable para usarlo dsp
print(sum_div)#imprimi la nueva variable

