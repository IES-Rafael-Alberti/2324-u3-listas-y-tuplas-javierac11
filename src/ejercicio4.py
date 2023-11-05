#Ejercicio 3.1.4¶
#Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, 
#los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.

def leeNumero():
    numero = input("Introduce un numero: ")
    if not str.isdigit(numero):
        raise ValueError
    return int(numero)

def leeNumeros():
    numeros = []
    for _ in range(5):
        numero = leeNumero()
        numeros.append(numero)
    return numeros

if __name__ == '__main__':
    numeros = leeNumeros()
    
    numeros_ordenados = sorted(numeros)
    
    print(numeros_ordenados)