def eliminar_subcadena(cadena, posicion, cantidad):

    return cadena[:posicion] + cadena[posicion + cantidad:]

if __name__ == "__main__":
    cadena_usuario = input("Ingresa la cadena de caracteres: ")
    
    try:
        posicion = int(input("Ingresa la posición desde la cual eliminar (entero): "))
        cantidad = int(input("Ingresa la cantidad de caracteres a eliminar (entero): "))
        
# Verifica que la posición y la cantidad son válidas
        if posicion < 0 or cantidad < 0 or posicion >= len(cadena_usuario):
            print("Posición o cantidad no válidas.")
        else:
#Elimina la subcadena y mostrar el resultado
            resultado = eliminar_subcadena(cadena_usuario, posicion, cantidad)
            print("Cadena resultante:", resultado)
    except ValueError:
        print("Por favor, ingresa valores enteros válidos.")
