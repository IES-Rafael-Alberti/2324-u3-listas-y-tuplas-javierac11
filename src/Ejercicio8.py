#Ejercicio 3.1.8¶
#Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.

def compruebaPalindromo(palabra):
    if palabra == palabra[::-1]:
        return True
    else:
        return False

if __name__ == '__main__':
    palabra = input("Introduce una palabra: ")
    if compruebaPalindromo(palabra):
        print("Es un palindromo")
    else:
        print("No es un palindromo")