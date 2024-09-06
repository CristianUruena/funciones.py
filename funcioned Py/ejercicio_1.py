def mayor_estricto(a, b, c):
    max_value = max(a, b, c)

    if (a == max_value) + (b == max_value) + (c == max_value) == 1:
        return max_value
    else:
        return -1

if __name__ == "__main__":
    try:
        a = float(input("Ingresa el primer número positivo: "))
        b = float(input("Ingresa el segundo número positivo: "))
        c = float(input("Ingresa el tercer número positivo: "))
        
        if a > 0 and b > 0 and c > 0:
            resultado = mayor_estricto(a, b, c)
            
            if resultado != -1:
                print(f"El mayor número estricto es: {resultado}")
            else:
                print("No existe un mayor estricto.")
        else:
            print("Por favor, ingresa solo números positivos.")
    except ValueError:
        print("Por favor, ingresa valores numéricos válidos.")
