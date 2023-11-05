#Ejercicio 3.1.1¶
#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, 
#Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.

def printaAsignatura(asignaturas: list):
    """Recoge una lista de asignaturas y la muestra por pantalla

    Args:
        asignaturas (list): Una lista de las asignaturas

    Returns:
        None: esta funcion no devuelve nada solo imprime
    """
    
    for asignatura in asignaturas:
        print(asignatura)
    return asignatura
    
if __name__ == "__main__":
    printaAsignatura(["Matemáticas", "Física", "Química", "Historia", "Lengua"])