def cambiaCero(lista,x):
    for i in range(len(lista)):
        if lista[i]<x:
            lista[i]=0
    print(lista)

s = [1, 4.1, 6.3, 2, 3.2, 8] 
cambiaCero(s,3)   

