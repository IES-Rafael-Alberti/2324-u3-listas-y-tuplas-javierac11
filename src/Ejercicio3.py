#Ejercicio 3.1.3¶
#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas,
# Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado 
# en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has 
# sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada 
# una de las correspondientes notas introducidas por el usuario.

def leeNota(asignatura: str):
    """Lee la nota que tiene

    Args:
        asignatura (str): la asignatura que quieres que aparezca en el input

    Raises:
        TypeError: Error si no se puede convertir en float

    Returns:
        float: La nota que se ha introducido
    """
    nota = input(f"Introduce la nota de {asignatura}: ")
    try:
        nota = float(nota)
        return nota
    except:
        raise TypeError

def generaMensaje(asignatura: str, nota: float): #-> str:
    """Genera el mensaje con la asignatura y la nota 

    Args:
        asignatura (str): La asignatura para el mensaje 
        nota (float): La nota para el mensaje

    Returns:
        str: Devuelve el mensaje con el siguiente mensaje "En {asignatura} has sacado {nota}"
    """
    
    return f"En {asignatura} has sacado {nota}"

def generaMensajes(asignaturas: list):
    """Introduce una lista con las asignaturas, te pide la nota 

    Args:
        asignaturas (list): Una lista con las asignaturas que tiene

    Returns:
        list: una lista con lops mensajes
    """
    
    mensajes = []
    
    for asignatura in asignaturas:
        nota = leeNota(asignatura)
        mensajes.append(generaMensaje(asignatura, nota))
    
    return mensajes

def printaMensaje(mensajes):
    for mensaje in mensajes:
        print(mensaje)

if __name__ == '__main__':
    try:
        mensajes = generaMensajes(["Matemáticas", "Física", "Química", "Historia", "Lengua"])
        printaMensaje(mensajes)
    except:
        print("ERROR")