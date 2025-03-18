dinero = int(input("Ingrese el monto a retirar "))
mil = dinero//1000 #billetes de 1000
rmil = dinero%1000 #lo que me sobra del dinero ingresado

cien = rmil//100 #divido lo que sobro por 100, dando los billetes de 100 q va a dar
rcien = rmil%100 #me da el resto de mil divido por 100
 
diez = rcien//10 #divido lo que sobro de 100 por 10
rdiez = rcien%10 #me da el resto de 100 divido por 10  

uno = rdiez//1 #divido lo que sobro de 100 por 1

print(mil,"billetes de $1000",cien,"billetes de $100",diez,"billetes de $10",uno,"monedas de un $1")

print(rmil)