# test_analizador.py

from analizador import contar_frecuencias

def test_frecuencias_basico():
    resultado = contar_frecuencias("sol luna sol")
    assert resultado["sol"] == 2
    assert resultado["luna"] == 1

def test_frecuencias_vacio():
    resultado = contar_frecuencias("")
    assert resultado == {}

def test_frecuencias_mayusculas():
    resultado = contar_frecuencias("Sol sol SOL")
    assert resultado["sol"] == 3
    # TODO: completa la asercion que verifica que las tres variantes de
    # "sol" (con distintas mayusculas) se cuentan como la MISMA palabra,
    # gracias al .lower() de la funcion. El resultado deberia tener
    # "sol": 3

#Prueba que la funcion cuente correctamente palabras separadas por 
# tabulaciones y saltos de linea
def test_tabulaciones_y_saltos_de_linea():
    resultado = contar_frecuencias("sol\nsol\tsol sol    sol")
    assert resultado["sol"] == 5