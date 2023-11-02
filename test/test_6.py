from src.Ejercicio6 import eliminaAprobados

notas = [1.0, 5, 4.9, 6, 10]
def mock_notas(s):
    return notas.pop(0)

def test_eliminaAprobados(monkeypatch):
    monkeypatch.setattr('builtins.input', mock_notas)
    assert eliminaAprobados(["Matemáticas", "Física", "Química", "Historia", "Lengua"]) == ["Matemáticas", "Química"]