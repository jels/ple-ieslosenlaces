"""
Calcula letra DNI

"""

from easygui import *

LETRAS = "TRWAGMYFPDXBNJZSQVHLCKE"

dni = enterbox("Introduzca DNI:")

resto = int(dni) % 23

msgbox( dni +  '-' + LETRAS[resto], title="Letra NIF", ok_button="Aceptar")
