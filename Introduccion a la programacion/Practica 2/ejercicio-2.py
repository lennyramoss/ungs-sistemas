"""edad = int(input("Ingrese su edad "))
distancia = int(input("Ingrese su distancia con el centro de votacion "))

if edad>70: 
    print("No tenes que votar, ya sos mayor de 70 años.")
elif edad<=18:
    print("Sos menor de edad.")
elif distancia>500:
    print("No tenes que votar, vivis a mas de 500km del centro de votacion.")
else:
    print("Tenes que votar")
"""

(edad >70) or (18<=edad<=70 and distancia>500)