import pytest
from src.main import (validar_rut, validar_direccion, validar_correo, 
                          validar_edad, validar_genero, validar_prevision_social)

def test_validar_rut():
    assert validar_rut(5000000) == True
    assert validar_rut(99999999) == True
    assert validar_rut(1234567) == False
    assert validar_rut(100000000) == False
    assert validar_rut('12345678') == False

def test_validar_direccion():
    assert validar_direccion("Av. Siempre Viva 742") == True
    assert validar_direccion("a" * 100) == True
    assert validar_direccion("a" * 101) == False
    assert validar_direccion(123456) == False

def test_validar_correo():
    assert validar_correo("example@example.com") == True
    assert validar_correo("example.com") == False
    assert validar_correo("example@com") == True
    assert validar_correo("") == False

def test_validar_edad():
    assert validar_edad(0) == True
    assert validar_edad(125) == True
    assert validar_edad(-1) == False
    assert validar_edad(126) == False
    assert validar_edad("20") == False

def test_validar_genero():
    assert validar_genero('f') == True  # El género 'f' es válido
    assert validar_genero('F') == True  # El género 'F' es válido
    assert validar_genero('m') == True  # El género 'm' es válido
    assert validar_genero('M') == True  # El género 'M' es válido
    assert validar_genero('n') == True  # El género 'n' es válido
    assert validar_genero('N') == True  # El género 'N' es válido
    assert validar_genero('x') == False  # El género 'x' no es válido
    assert validar_genero('F ') == False  # El género 'F ' (con espacio) no es válido
    assert validar_genero('') == False  # El género vacío no es válido

if __name__ == "__main__":
    import pytest
    pytest.main([__file__])

def test_validar_prevision_social():
    assert validar_prevision_social('ISAPRE') == True
    assert validar_prevision_social('FONASA') == True
    assert validar_prevision_social('isapre') == False
    assert validar_prevision_social('Fonasa') == False
    assert validar_prevision_social('') == False
