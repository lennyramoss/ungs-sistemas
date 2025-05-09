a = float(input("Ingrese la primer nota "))
b = float(input("Ingrese la segunda nota "))
c = float(input("Ingrese la tercer nota "))
nf = (a+b+c) / 3
if nf > 10:
    print("Ingrese una nota valida")
elif nf >=0 and nf <4:
    print("Recursdo")
elif nf >=4 and nf <7:
    print("Debe rendir examen final")
else:
    print("Eximido")