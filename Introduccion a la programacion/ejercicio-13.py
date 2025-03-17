capital = int(input("Ingrese su capital "))
mes = int(input("Cuantos meses quiere invertir "))
inversion = (capital*6)/100 * mes
capital = capital+inversion
print("Su capital aumento a", capital)
