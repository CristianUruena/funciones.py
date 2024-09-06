es_par = lambda x: x % 2 == 0

if __name__ == "__main__":
    try:
        valor = int(input("Ingresa un número para comprobar si es par o impar: "))
        
        if es_par(valor):
            print(f"El número {valor} es par.")
        else:
            print(f"El número {valor} es impar.")
    except ValueError:
        print("Por favor, ingresa un valor entero válido.")
