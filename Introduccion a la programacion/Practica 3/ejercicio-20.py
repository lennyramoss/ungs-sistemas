m = int(input("Ingrese el valor m: "))
n = int(input("Ingrese el valor n: "))


if n>m:
    for i in range(m, n + 1):
        for j in range(i, n + 1):  # empieza en i para evitar los inversos
            print(i, j)
elif n<m:
    for i in range(m, n + 1):
        for j in range(i, n + 1):  # empieza en i para evitar los inversos
            print(i, j)
else:
    print(m, n)



