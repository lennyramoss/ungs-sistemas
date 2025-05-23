palabra = input("Ingrese una palabra ").lower()
ya_contadas = ""  # Para registrar las letras que ya analizamos

for letra in palabra:# Recorre cada letra de la palabra ingresada
    if letra != " " and letra not in ya_contadas:#que no sea un espacio y Que la letra no haya sido contada antes
        contador = 0
        for caracter in palabra:
            if caracter == letra:
                contador += 1
        print(f"{letra} : {contador}")
        ya_contadas += letra  # Marcamos la letra como ya contada
