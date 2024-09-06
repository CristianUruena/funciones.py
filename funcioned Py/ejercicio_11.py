def imprimir_centrada(cadena, ancho=80):

    cadena_centrada = cadena.center(ancho)
    print(cadena_centrada)

# Programa principal
if __name__ == "__main__":

    cadena_usuario = input("Ingresa una cadena de caracteres: ")
    
    imprimir_centrada(cadena_usuario)
