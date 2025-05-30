#1

def ventaEntradas(salas,peliculas,capacidad):
    indice=0
    print(peliculas)
    pelicula = str(input("Eliga que pelicula desea ver dentro del a siguiente lista "))
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

"""2)La biblioteca de la universidad asigna un código a cada libro que posee, el mismo se conforma con las 
consonantes  del  título  que  no  estén  repetidas  y  exactamente  4  dígitos  con  la  cantidad  de  páginas,  en 
caso de tener más de 9999 páginas se mostrarán los últimos dígitos.  Ejemplo:  Título: “eternamente” Cantidad de hojas: 918    Salida: “RM0918” 
Hacer una función que reciba el título y la cantidad de páginas de un libro y devuelva el código."""


def codigoLibro(nombre,pags):
    noConsonantes=["a","e","i","o","u"]
    consonantesPalabra=[]
    codigo=""
    pags = str(pags)
    cero="0"
    

    #SIEMPRE QUE BUSCO VER SI LA LETRA APARECE MAS DE UNA SOLA VEZ
    #DEBO RECORRER CADA LETRA Y LUEGO HACER OTRO FOR QUE RECORRA TODAS LAS LETRAS
    for letra in nombre:
        if letra not in noConsonantes:
            consonantesPalabra.append(letra)
    print(consonantesPalabra)

    for letra in consonantesPalabra:
        cont=0
        for char in consonantesPalabra:
            if letra == char:
                cont+=1
        if cont==1:
            codigo+=letra
    print(codigo)

    if len(pags)==5 or len(pags)==6:
        codigo+="9999"
    elif len(pags)==4:
        codigo+=pags
    i=3
    c=1        
    while len(pags)<=i:
        if len(pags)==i:
            codigo+=cero*c+pags
        i-=1
        c+=1
    print(codigo)

codigoLibro("eternamente",123)

