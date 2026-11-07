
from analizador import contar_frecuencias

def test_frecuencias_basico():
    resultado = contar_frecuencias("casa auto casa auto auto")
    assert resultado["casa"] == 2
    assert resultado["auto"] == 3

def test_frecuencias_vacio():
    resultado = contar_frecuencias("")
    assert resultado == {}

def test_frecuencias_mayusculas():
    resultado = contar_frecuencias("CASA casa Auto AUTO cAsA")
    assert resultado["casa"] == 3
    assert resultado["auto"] == 2