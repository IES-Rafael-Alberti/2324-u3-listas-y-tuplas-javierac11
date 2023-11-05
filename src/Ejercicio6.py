#Ejercicio 3.1.6¶
#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química,
#Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine 
#de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que
#el usuario tiene que repetir.

def leeNota(asignatura):
    nota = input(f"Introduce la nota de {asignatura}: ")
    try:
        nota = float(nota)
        if nota > 10 or nota < 0:
            raise ValueError
        return nota
    except:
        raise TypeError
    
def comprobarAprobado(nota):
    if nota >= 5:
        return True
    else:
        return False

def eliminaAprobados(asignaturas): 
    asignaturas_suspensas = []
    for asignatura in asignaturas:
        nota = leeNota(asignatura)
        if not comprobarAprobado(nota):
            asignaturas_suspensas.append(asignatura)
    return asignaturas_suspensas

if __name__ == '__main__':
    
    asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"] 
    asignaturas = eliminaAprobados(asignaturas)   
    
    print(asignaturas)