def calcular_cambio(total_compra, dinero_recibido):
    if dinero_recibido < total_compra:
        return "Error: El dinero recibido es insuficiente."
    
    denominaciones = [500, 100, 50, 20, 10, 5, 1]
    
    vuelto = dinero_recibido - total_compra
    resultado = {}
    
    for valor in denominaciones:
        cantidad_billetes = vuelto // valor
        if cantidad_billetes > 0:
            resultado[valor] = cantidad_billetes
            vuelto %= valor
    
    return resultado

if __name__ == "__main__":
    try:
        total_compra = int(input("Ingresa el total de la compra: "))
        dinero_recibido = int(input("Ingresa el dinero recibido: "))
        
        resultado = calcular_cambio(total_compra, dinero_recibido)
        
        if isinstance(resultado, str):
            print(resultado)
        else:
            print("Cambio a devolver:")
            for denominacion, cantidad in resultado.items():
                print(f"${denominacion}: {cantidad} billete(s)")
    except ValueError:
        print("Por favor, ingresa solo números enteros.")
