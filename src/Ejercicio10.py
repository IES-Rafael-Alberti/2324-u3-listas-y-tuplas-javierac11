#Ejercicio 3.1.10¶
#Escribir un programa que almacene en una lista los siguientes precios: 50, 75, 46, 22, 80, 65, 8 
# y muestre por pantalla el menor y el mayor de los precios.

def mayorMenor(lista: list):
    lista.sort()
    
    menor = lista[0]
    mayor = lista[len(lista)-1]
    return menor, mayor
    
if __name__ == '__main__':
    lista = [50, 75, 46, 22, 80, 65, 8]
    print(mayorMenor(lista))