#Ejercicio 3.1.9¶
#Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.

def contarLetras(palabra, letra):
    total_letras = palabra.count(letra)
    return total_letras

if __name__ == '__main__':
    palabra = input("Introduce una palabra: ")
    letra = input("Introduce una letra: ")
    print(f"{palabra} tiene {contarLetras(palabra, letra)} {letra}")