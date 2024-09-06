def cuadrados_hasta_n(n):
    #lista con los cuadrados de los números entre 1 y N (inclusive)
    lista_cuadrados = [i ** 2 for i in range(1, n + 1)]
    return lista_cuadrados

def imprimir_ultimos_10(valores):
    # Imprime los últimos 10 valores de la lista
    if len(valores) <= 10:
        print(valores)  # Si hay 10 o menos valores, se imprimen todos
    else:
        print(valores[-10:])  # Imprimir los últimos 10 valores

if __name__ == "__main__":
    try:
        # Ingresar el valor de N
        n = int(input("Ingresa un número N: "))
        
        if n <= 0:
            print("Por favor, ingresa un número entero positivo.")
        else:

            lista_cuadrados = cuadrados_hasta_n(n)
            print("Últimos 10 valores de la lista de cuadrados:")
            imprimir_ultimos_10(lista_cuadrados)
    except ValueError:
        print("Por favor, ingresa un valor entero válido.")
