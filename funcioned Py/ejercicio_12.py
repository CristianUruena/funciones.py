def fecha_extendida(fecha):

    dias = fecha[0]
    mes = fecha[1]
    año = fecha[2]

    # Lista de nombres de los meses
    nombres_meses = [
        "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
        "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
    ]

    if 1 <= mes <= 12:
        nombre_mes = nombres_meses[mes - 1]
    else:
        return "Mes no válido"

    # Devuelv la fecha en formato extendido
    return f"{dias} de {nombre_mes} de {año}"

if __name__ == "__main__":
    try:
        dia = int(input("Ingresa el día (número entero): "))
        mes = int(input("Ingresa el mes (número entero): "))
        año = int(input("Ingresa el año (número entero): "))
        
        # tupla de fecha
        fecha_usuario = (dia, mes, año)
        
        # fecha en formato extendido
        resultado = fecha_extendida(fecha_usuario)
        print(resultado)
    except ValueError:
        print("Por favor, ingresa valores enteros válidos.")
