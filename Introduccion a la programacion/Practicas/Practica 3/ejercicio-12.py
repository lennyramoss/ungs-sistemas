m = int(input("Ingrese un numero "))
suma = 0
n = 1


while suma<=m:
    suma+=n
    n+=1
print("El primer n para el cual la suma supera a", m, "es:", n - 1)