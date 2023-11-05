from src.Ejercicio3 import leeNota, generaMensaje, generaMensajes
import pytest

def test_leeNota(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "6")
    assert leeNota("Lengua") == 6.00
    
def test_leeNota_error(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'abc')
    with pytest.raises(TypeError):
        leeNota()
        
def test_generaMensaje():
    assert generaMensaje("lengua", 7.00) ==  "En lengua has sacado 7.0"
    
entradas = [1.5, 7.0, 9.9]
    
def mock_generaMensajes(s):
    return entradas.pop(0)
    
def test_generaMensajes(monkeypatch):
    monkeypatch.setattr('builtins.input', mock_generaMensajes)
    assert generaMensajes(["Matemáticas", "Física", "Química"]) == ["En Matemáticas has sacado 1.5", "En Física has sacado 7.0", "En Química has sacado 9.9"]