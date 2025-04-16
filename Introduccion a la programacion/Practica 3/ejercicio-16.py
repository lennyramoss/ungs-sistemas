n = int(input("Ingrese la cantidad de terminos que desea usar "))
denom = 1
signo = 1
suma = 0
for i in range (n): #llega hasta n. si ingreso 5, arranca en 0 y lo hace hasta 4(ej)
    cuenta = (1*signo)/denom
    suma += cuenta
    denom = denom+2 #incrementa el valor de denominador +2
    signo *= -1 #signo vale -1 asi la cuenta da negativa
aproximacion_pi = suma * 4
print(suma)