def procesar_frase(frase):
    
    palabras = frase.split()
    
    # eliminar palabras duplicadas
    palabras_unicas = set(palabras)
    
    # lista para poder ordenar
    palabras_unicas_lista = list(palabras_unicas)
    
    # palabras ordenadas por longitud
    palabras_ordenadas = sorted(palabras_unicas_lista, key=len)
    
    return palabras_ordenadas

if __name__ == "__main__":
    frase_usuario = input("Ingresa una frase: ")
    
    resultado = procesar_frase(frase_usuario)
    
    print("Palabras ordenadas por longitud:")
    for palabra in resultado:
        print(palabra)
