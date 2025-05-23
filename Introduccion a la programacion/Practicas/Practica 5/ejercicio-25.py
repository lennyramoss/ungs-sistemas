"""Hacer una función que automatice el control vehicular en rutas nacionales. Hacer el control
para la Ruta Nacional 8 durante un día completo, se deb e controlar que los automóviles no
sup eren 100 km/h y en caso de hacerlo se les enviará una multa a sus hogares, si es reincidente
la multa se duplica. Para ello cuenta con las siguientes funciones.
darPatentes(ruta): Dada una ruta nacional devuelve una lista con to das las patentes de los
autos que pasaron en el día.
controlVelocidad(patente): Recib e un número de patente y devuelve la velo cidad a la que
cruzó el radar dicho automóvil.
reincidente(patente): Devuelve True en caso de que la patente ya tenga multas p or exceso
de velo cidad.
costoActual(): No recib e parámetros y devuelve el costo p or sup erar la velo cidad p ermitida.
enviarMulta(patente, costo): Manda una multa al domicilio del propietario del automóvil
con el costo.
"""

"""
darPatentes(ruta): Dada una ruta nacional devuelve una lista con to das las patentes de los
autos que pasaron en el día.
controlVelocidad(patente): Recib e un número de patente y devuelve la velo cidad a la que
cruzó el radar dicho automóvil.
reincidente(patente): Devuelve True en caso de que la patente ya tenga multas p or exceso
de velo cidad.
costoActual(): No recib e parámetros y devuelve el costo p or sup erar la velo cidad p ermitida.
enviarMulta(patente, costo): Manda una multa al domicilio del propietario del automóvil
con el costo
"""
def autoMultas(ruta):
    patentesHoy=darPatentes(ruta)
    multa=0

    for patente in patentesHoy:
        if controlVelocidad(patente)>100:
            if reincidente(patente):
                multa=costoActual()*2
                enviarMulta(patente,multa)
            else:
                multa=costoActual()
                enviarMulta(patente,multa)


                


