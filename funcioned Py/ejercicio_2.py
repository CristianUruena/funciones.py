def fecha_valida(dia, mes, año):
    
    meses_31 = [1, 3, 5, 7, 8, 10, 12]

    meses_30 = [4, 6, 9, 11]
    
    # Verificar que el año sea positivo
    if año <= 0:
        return False
    
    # Verificar que el mes esté entre 1 y 12
    if mes < 1 or mes > 12:
        return False
    
    # Verificar los días dependiendo del mes
    if mes in meses_31:
        return 1 <= dia <= 31
    elif mes in meses_30:
        return 1 <= dia <= 30
    elif mes == 2:  
        # Verificar si es año bisiesto
        if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
            return 1 <= dia <= 29
        else:
            return 1 <= dia <= 28
    return False

if __name__ == "__main__":
    try:
        dia = int(input("Ingresa el día: "))
        mes = int(input("Ingresa el mes: "))
        año = int(input("Ingresa el año: "))
        
        if fecha_valida(dia, mes, año):
            print("La fecha ingresada es válida.")
        else:
            print("La fecha ingresada no es válida.")
    except ValueError:
        print("Por favor, ingresa solo números enteros positivos.")
