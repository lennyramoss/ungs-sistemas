base = 480
precio = 25.5
impuestos = 78
consumo = int(input("Ingrese su consumo "))

if consumo>200:
    consumo -= 200
    consumo *= precio + impuestos + base 
    print("Tiene que pagar:", consumo)
else:
    print("Tiene que pagar:", base + impuestos)