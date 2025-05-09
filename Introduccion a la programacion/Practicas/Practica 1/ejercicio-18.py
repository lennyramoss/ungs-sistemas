dato = int(input("Ingrese la cantidad de segundos "))

dias = dato//86400
rd = dato%86400

hs = rd//3600
rhs = rd%3600

mins = rhs//60
rm = rhs%60

print (dias,"Dia",hs,"horas",mins,"minutos",rm,"segundos")