def ordenada(lista):

    return all(lista[i] <= lista[i + 1] for i in range(len(lista) - 1))

# verificar el comportamiento de la función
if __name__ == "__main__":

    entrada = input("Ingresa una lista de elementos (separados por comas): ")
    
    try:
        # Evalua la entrada para convertirla en una lista de números o caracteres
        lista = eval(entrada)
        
        if isinstance(lista, list):
            # Verifica si la lista está ordenada
            resultado = ordenada(lista)
            
            if resultado:
                print("La lista está ordenada en forma ascendente.")
            else:
                print("La lista no está ordenada en forma ascendente.")
        else:
            print("Por favor, ingresa una lista válida.")
    except (SyntaxError, ValueError, TypeError):
        print("Por favor, ingresa una lista válida de números o caracteres.")
