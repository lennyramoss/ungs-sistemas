a = int(input("Ingrese la primer nota "))
b = int(input("Ingrese la segunda nota "))
c = int(input("Ingrese la tercer nota "))
nf = (a+b+c) / 3
if nf > 10:
    print("Ingrese una nota valida")
elif nf >=0 and nf <4:
    print("Recursaste")
elif nf >=4 and nf <7:
    print("Vas a final")
else:
    print("Promocionaste")

