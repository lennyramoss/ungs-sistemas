def laMasCorta():
    if len(autos)>len(motos):
        print(f"la lista mas larga es autos:{autos}")
    elif len(autos)<len(motos):
        print(f"la lista mas larga es motos:{motos}")
    else:
        print("las listas tienen la misma cantidad de elementos")




autos = ["ford","toyota","chevrolet","bmw"]
motos = ["yamaha","kawasaki"]

laMasCorta()