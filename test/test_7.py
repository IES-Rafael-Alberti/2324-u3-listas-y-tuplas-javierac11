from src.Ejercicio7 import generaAbecedario, eliminarMultiplosDe3

def test_generaAbecedario():
    assert generaAbecedario() == ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def test_emininaMultiplosDe3():
    abecedario = generaAbecedario()
    assert eliminarMultiplosDe3(abecedario) == ['b', 'c', 'e', 'f', 'h', 'i', 'k', 'l', 'n', 'o', 'q', 'r', 't', 'u', 'w', 'x', 'z']