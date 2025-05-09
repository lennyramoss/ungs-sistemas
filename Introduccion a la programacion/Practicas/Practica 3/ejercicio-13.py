n = int(input("Ingrese cuantos terminos desea ver "))

print("Sucesión an = 2n:")
for i in range(1,n+1):
    resultado= 2*i
    print(resultado)

print("Sucesión an = 2n - 1:")
for i in range(1,n+1):
    resultado= 2*i-1
    print(resultado)

print("Sucesión an = n^2:")
for i in range(1,n+1):
    resultado= i**2
    print(resultado)

print("Sucesión an = n^3 - n^2:")
for i in range(1,n+1):
    resultado= i**3 - i**2
    print(resultado)

print("Sucesión an = 1/n^2:")
for i in range(1,n+1):
    resultado= 1/(i**2)
    print(resultado)
