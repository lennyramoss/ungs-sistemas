x= int(input("Ingrese un numero "))
y= int(input("Ingrese segundo numero "))
z= int(input("Ingrese un tercer numero "))
print("Valores sin alterar",x,y,z)
aux1=x
aux2=z
x = y
y = aux2
z=aux1



print("Valores alterados",x,y,z)


