
for a in range(-10, 11):
    for b in range(-10, 11):
        for c in range(-10, 11):
            if a == 0 or b == 0 or c == 0:
                print("Alguno es cero")  
            elif a == b or b == c or a == c:
                print("Hay números repetidos")  
            elif a + b + c == a * b * c:
                print(f"Solución encontrada: A = {a}, B = {b}, C = {c}")





                #CAMBIAR PRINTS