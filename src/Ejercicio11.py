#Ejercicio 3.1.11¶
#Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre por pantalla su producto escalar.

def productoEscalar(vector1: tuple, vector2: tuple):
    producto_escalar = 0
    if len(vector1) != len(vector2):
        raise IndexError
    for x in range(len(vector1)):
        producto_escalar += vector1[x]*vector2[x]
    return producto_escalar
        
if __name__ == '__main__':
    vector1 = (1,2,3)
    vector2 = (-1,0,2)
    print(productoEscalar(vector1, vector2))