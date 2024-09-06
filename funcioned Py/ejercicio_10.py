def es_capicua(cadena):

    cadena = cadena.lower()
    #longitud de la cadena
    longitud = len(cadena)
    
    # Compara caracteres desde los extremos hacia el centro
    for i in range(longitud // 2):
        if cadena[i] != cadena[longitud - 1 - i]:
            return False
    return True

# verificar el funcionamiento de la función
if __name__ == "__main__":

    cadena = input("Ingresa una cadena de caracteres para verificar si es capicúa: ")
    
    # Verifica si la cadena es capicúa
    if es_capicua(cadena):
        print(f"La cadena '{cadena}' es capicúa.")
    else:
        print(f"La cadena '{cadena}' no es capicúa.")
