dinero = int(input("Ingrese el monto a retirar "))
veint =  dinero//20000 #billetes de 20000
rveint= dinero%20000 #lo que me sobra del dinero ingresado

dmil = rveint//10000
rdmil = rveint%10000

mil = rdmil//1000
rmil = rdmil%1000

cien = rmil//100 #divido lo que sobro por 100, dando los billetes de 100 q va a dar
rcien = rmil%100 #me da el resto de mil divido por 100

diez = rcien//10 #divido lo que sobro de 100 por 10
rdiez = rcien%10 #me da el resto de 100 divido por 10

uno = rdiez//1 #divido lo que sobro de 100 por 1

print(veint,"billetes de $20000",dmil,"billetes de $10000",mil,"billetes de $1000",cien,"billetes de $100",diez,"billetes de $10",uno,"monedas de un $1")

print(rmil)