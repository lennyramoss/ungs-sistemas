m = int(input("Ingrese el valor m: "))
n = int(input("Ingrese el valor n: "))


if n>m:
    for i in range(m, n + 1):
        for j in range(m, n + 1):
            print(i, j)
elif n<m:
    for i in range(n, m + 1):
        for j in range(n, m + 1):
            print(i, j)
else:
    print(m, n)

#b










"""m = int(input("Ingrese el valor m: "))
n = int(input("Ingrese el valor n: "))

inicio = min(m, n)
fin = max(m, n)

for i in range(inicio, fin + 1):
    for j in range(inicio, fin + 1):
        print(i, j)
"""