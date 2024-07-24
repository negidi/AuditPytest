import re

def validar_rut(rut):
    if isinstance(rut, int) and 5000000 <= rut <= 99999999:
        return True
    return False

def validar_direccion(direccion):
    if isinstance(direccion, str) and len(direccion) <= 100:
        return True
    return False

def validar_correo(correo):
    if isinstance(correo, str) and "@" in correo:
        return True
    return False

def validar_edad(edad):
    if isinstance(edad, int) and 0 <= edad <= 125:
        return True
    return False

def validar_genero(genero):
    if isinstance(genero, str) and genero.lower() in ['f', 'm', 'n', 'F', 'M', 'N']:
        return True
    return False

def validar_prevision_social(prevision):
    if isinstance(prevision, str) and prevision in ['ISAPRE', 'FONASA']:
        return True
    return False
