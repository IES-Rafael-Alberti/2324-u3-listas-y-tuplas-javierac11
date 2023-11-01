from src.Ejercicio2 import generaMensaje

def test_generaMensaje():
    assert generaMensaje(["Matemáticas", "Física", "Química", "Historia", "Lengua"]) == ['Yo estudio Matemáticas', 'Yo estudio Física', 'Yo estudio Química', 'Yo estudio Historia', 'Yo estudio Lengua']