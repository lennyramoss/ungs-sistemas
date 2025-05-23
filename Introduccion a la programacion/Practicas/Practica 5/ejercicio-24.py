"""plan oro usos ilimitados
plan plata 5 usos
cobertura(cliente): retorna un string con los valores "Oro" o "Plata", correspon-
diente al tipo de cobertura del cliente.

usados(cliente): retorna un entero que representa la cantidad de servicios que
ya utilizó el cliente.

radioDeCobertura(cliente, localidad): devuelve True si el cliente se encuentra
dentro del radio de cobertura cubierto por la empresa."""

#ORO si esta dentro del area de cobertura, si esta fuera 30$ listo
#PLATA si le quedan servicios y esta dentro de la zona pagan 50$, si esta fuera del area +30$


def pagara(nroCliente,localidadCliente):
    if cobertura(nroCliente)=="Oro":
        if radioDeCobertura(nroCliente,localidadCliente):
            return 0
        elif not radioDeCobertura(nroCliente,localidadCliente):
            return 30 
    
    if cobertura(nroCliente)=="Plata":
        if usados(nroCliente)>5 and radioDeCobertura(nroCliente,localidadCliente):
            return 50
        elif usados(nroCliente)<=5 and not radioDeCobertura(nroCliente,localidadCliente):
            return 80

nroCliente= int(input("Ingrese el numero de cliente"))
localidadCliente = str(input("Ingrese su localidad"))
cuantoPagara=pagara(nroCliente,localidadCliente)
