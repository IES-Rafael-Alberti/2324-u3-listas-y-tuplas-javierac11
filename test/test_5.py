from src.Ejercicio5 import generaMensaje

def test_generaMensaje():
    assert generaMensaje([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == "10, 9, 8, 7, 6, 5, 4, 3, 2, 1"