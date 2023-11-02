from src.ejercicio4 import leeNumeros
import pytest

entrada = ["5", "8", "52", "6", "9"]

def mock_leenumeros(s):
    return entrada.pop(0)

def test_leenumeros(monkeypatch):
    monkeypatch.setattr('builtins.input', mock_leenumeros)
    assert leeNumeros() == [5, 8, 52, 6, 9]
    

entrada_error = ["5", "8", "e", "6", "9"]

def mock_leenumeros_error(s):
    return entrada_error.pop(0)
    
def test_leenumeros_error(monkeypatch):
    monkeypatch.setattr('builtins.input', mock_leenumeros_error)
    with pytest.raises(ValueError):
        leeNumeros()