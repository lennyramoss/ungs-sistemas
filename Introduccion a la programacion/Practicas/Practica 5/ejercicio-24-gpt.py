def pagara(cliente, localidad):
    tipo = cobertura(cliente)           # "Oro" o "Plata"
    cantidad_usos = usados(cliente)     # número entero
    en_cobertura = radioDeCobertura(cliente, localidad)  # True o False

    costo = 0

    if tipo == "Oro":
        if not en_cobertura:
            costo += 30  # Oro solo paga si está fuera del área de cobertura
    elif tipo == "Plata":
        if not en_cobertura:
            costo += 30  # Siempre paga $30 si está fuera del área
        if cantidad_usos >= 5:
            costo += 50  # Si ya usó los 5, paga $50 (además del $30 si aplica)

    return costo


