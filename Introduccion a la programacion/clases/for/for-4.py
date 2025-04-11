cantidad = int(input("Ingrese cuantas notas va a ingresar "))
total = 0 
for i in range (cantidad):
    cal = int(input("Ingrese su nota "))
    total += cal
prom = total/cantidad
print("su promedio final es", prom)