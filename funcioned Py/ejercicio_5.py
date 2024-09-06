cuadrado = lambda x: x ** 2

if __name__ == "__main__":
    try:
        valor = float(input("Ingresa un número para calcular su cuadrado: "))
        
        resultado = cuadrado(valor)
        
        print(f"El cuadrado de {valor} es {resultado}.")
    except ValueError:
        print("Por favor, ingresa un valor numérico válido.")
