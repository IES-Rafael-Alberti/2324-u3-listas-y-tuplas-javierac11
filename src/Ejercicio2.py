#Ejercicio 3.1.2¶
#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas,
#Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje 
#Yo estudio <asignatura>, donde <asignatura> sobre cada una de las asignaturas de la lista.

def generaMensaje(asignaturas: list):
    """Se introduce una lista con las asignaturas y se devuelve una lista con los mensajes

    Args:
        asignaturas (list): Una lista con las asignaturas

    Returns:
        list: Una lista con los mensaje
    """
    asignaturas_modificada = []
    for asignatura in asignaturas:
        asignaturas_modificada.append(f"Yo estudio {asignatura}")
    
    return asignaturas_modificada

def printaMensaje(mensajes: list):
    """Recoge una lista de mensajes y los muestra por pantalla

    Args:
        mensajes (list): Una lista con los mensajes

    Returns:
        None: esta funcion no devuelve nada solo imprime
    """
    for mensaje in mensajes:
        print(mensaje)
        
if __name__ == "__main__":        
    asignaturas = generaMensaje(["Matemáticas", "Física", "Química", "Historia", "Lengua"])
    printaMensaje(asignaturas)