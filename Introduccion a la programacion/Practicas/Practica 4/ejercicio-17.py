def tieneRepetidas(palabra):
    for elemento in palabra:
        if cuantos(palabra,elemento)>=2:
            return True
    return False    

def cuantos(cadena, letra):
    cont=0
    for elemento in cadena:
        if elemento == letra:
            cont+=1
    return cont

tieneRepetidas("elefante")
