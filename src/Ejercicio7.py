#Ejercicio 3.1.7¶
#Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que 
#ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.

def generaAbecedario():
    abecedario = []
    for x in range(97, 123):
        letra = chr(x)
        abecedario.append(letra)
    return abecedario

def eliminarMultiplosDe3(abecedario):
    copia_abecedario = list.copy(abecedario)

    for i in range(len(abecedario)):
        if i % 3 == 0:
            copia_abecedario.remove(abecedario[i])
    return copia_abecedario

if __name__ == '__main__':
    abecedario = generaAbecedario()
    abecedario_sin_multiplos_3 = eliminarMultiplosDe3(abecedario)
    print(abecedario_sin_multiplos_3)