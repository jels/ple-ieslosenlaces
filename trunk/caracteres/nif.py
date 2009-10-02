"""
Calcula letra DNI

"""

LETRAS = "TRWAGMYFPDXBNJZSQVHLCKE"

dni = input("Introduzca DNI:")

resto = dni % 23

print dni, '-', LETRAS[resto]
