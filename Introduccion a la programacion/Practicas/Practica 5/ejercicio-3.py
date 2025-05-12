def divisores(numero):
    divisores_numero=[]
    for i in range(1,numero+1):      
        div=numero%i
        if div==0:
            divisores_numero.append(i)
    return divisores_numero

qwe=divisores(10)
print(qwe)

