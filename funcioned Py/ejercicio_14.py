def eliminar_claves(diccionario, claves):

    cantidad_inicial = len(diccionario)
    
#elimina las claves especificadas en la lista
    for clave in claves:
        if clave in diccionario:
            del diccionario[clave]
    
#Verifica si se elimino una clave
    cantidad_final = len(diccionario)
    exito = cantidad_inicial != cantidad_final
    
    return diccionario, exito

if __name__ == "__main__":
    diccionario = {
        "nombre": "Juan",
        "edad": 30,
        "ciudad": "Madrid",
        "ocupacion": "Ingeniero"
    }
    
    print("Diccionario original:", diccionario)
    
    claves_str = input("Ingresa las claves a eliminar separadas por comas: ")
    claves = [clave.strip() for clave in claves_str.split(",")]
    
# Elimina las claves del diccionario
    diccionario_modificado, exito = eliminar_claves(diccionario, claves)
    
    if exito:
        print("Diccionario modificado:", diccionario_modificado)
        print("Las claves fueron eliminadas con éxito.")
    else:
        print("No se eliminaron claves.")
