import re

def validar_correo(correo):
    """Retorna True si el correo sigue el patrón estándar."""
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(patron, correo))

def validar_rut(rut):
    """
    Agrega aquí tu lógica para validar el RUT chileno.
    Puedes usar expresiones regulares para el formato (XX.XXX.XXX-X).
    """
    patron_rut = r'^(\d{1,2}(\.\d{3}){2}-[\dkK])$'
    return bool(re.match(patron_rut, rut))