"""
1)Hacer una función que determine si un número ingresado por el usuario es un 
“número oblongo”. Indique también como la llamaría desde el programa principal. 
Número oblongo: todo número natural que cumple que es el producto de dos naturales 
consecutivos. Por ejemplo, los números 30, 42 y 56 son oblongos
"""
def oblongo(a):
    i=0
    while i*(i+1)<=a:
        if i*(i+1)==a:
            return True
        i+=1
    return False

n=int(input("Ingrese un numero "))
esOblongo=oblongo(n)
if esOblongo:
    print("es oblongo")
else:
    print("no es oblongo")


            


"""
2)Escribir un programa que le pida al usuario un conjunto de números y que 
encuentre la moda de los números introducidos (la moda de una muestra es el valor que 
más se repite en la muestra). Luego que indique las posiciones en donde se encuentran 
estos elementos y por último que muestre toda la lista ingresada por el usuario. 
"""

numeros=[]
numVistos=[]
cantidad = int(input("Ingrese la cantida de numeros "))
for i in range(cantidad):
    valores = int(input("Ingrese su numero "))
    numeros.append(valores)
print (numeros)



    
        


#3
palabra = input("Ingrese una palabra ").lower()
ya_contadas = ""  # Para registrar las letras que ya analizamos

for letra in palabra:# Recorre cada letra de la palabra ingresada
    if letra != " " and letra not in ya_contadas:#que no sea un espacio y Que la letra no haya sido contada antes
        contador = 0
        for caracter in palabra:#recorre los caracteres de la palabra comparando con la letra del primer for
            if caracter == letra: #si el caracter es igual a la letra del primer for
                contador += 1 #suma 1
        print(f"{letra} : {contador}")
        ya_contadas += letra  # Marcamos la letra como ya contada
          

#4