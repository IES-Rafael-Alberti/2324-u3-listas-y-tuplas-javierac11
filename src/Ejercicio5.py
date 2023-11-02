#Ejercicio 3.1.5¶
#Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso 
#separados por comas.

def generaMensaje(lista: list):
    mensaje = ""
    lista_invertida = list(reversed(lista))
    for numero in lista_invertida:
        if numero == lista_invertida[-1]:
            mensaje += f"{numero}"    
        else:
            mensaje += f"{numero}, "
    return mensaje
     
if __name__ == '__main__':
    print(generaMensaje([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))