def eliminar_palabras(lista_original, lista_a_eliminar):
    
    lista_resultante = [palabra for palabra in lista_original if palabra not in lista_a_eliminar]
    return lista_resultante

# Programapara ingresar las listas e imprimir los resultados
if __name__ == "__main__":
    # lista original de palabras
    lista_original = input("Ingresa la lista original de palabras (separadas por comas): ").split(',')
    lista_original = [palabra.strip() for palabra in lista_original]
    
    # Ingresar la lista de palabras a eliminar
    lista_a_eliminar = input("Ingresa la lista de palabras a eliminar (separadas por comas): ").split(',')
    lista_a_eliminar = [palabra.strip() for palabra in lista_a_eliminar] 
    
    # Eliminar las palabras de la lista original
    lista_resultante = eliminar_palabras(lista_original, lista_a_eliminar)
    

    print("Lista original:", lista_original)
    print("Lista de palabras a eliminar:", lista_a_eliminar)
    print("Lista resultante:", lista_resultante)
