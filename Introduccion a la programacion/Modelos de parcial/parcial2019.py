#1

def ventaEntradas(salas,peliculas,capacidad):
    indice=0
    pelicula = str(input("Eliga que pelicula desea ver dentro del a siguiente lista"))
    cant= int(input("Cuantas entradas desean "))


    for i in range(len(peliculas)):
        if peliculas[i] == pelicula:# COMPARO CADA UNA DE LAS POSICIONES CON EL NOMMBRE Q CARGO EL USUARIO
            indice = i


    if cant<=capacidad[indice]:
        print("su pelicula es en la sala",salas[indice])
        capacidad[indice]-=cant
        print(capacidad[indice])
    else:
        print("No hay mas capacidad para esta pelicula")

salass=[1,2,3,4,5,6]
peliculas=["xmen","titanic","saw","rio","taxi driver","avatar"]
capacidadDisponiblePorSala=[80,70,60,75,40,90]

ventaEntradas(salass,peliculas,capacidadDisponiblePorSala)


#practicar como usar if en los for 
#cuando usar cada for