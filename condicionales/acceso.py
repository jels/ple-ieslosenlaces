# -*- coding: cp1252 -*-
"""
Ejercicio con contraseñas
"""

from easygui import *
import sys

# password válida
valida = "megustapython"


# pedir datos 5 veces como máximo
# centinela
acierta = False
for x in range(5):
    passwd_usuario = passwordbox("Introduzca su contraseña", "Control de acceso")

    # comprobaciones
    # cancelación
    if passwd_usuario == None:
        msgbox("Operación cancelada")
        sys.exit()
    # válidar
    if passwd_usuario == valida:
        msgbox("Biennnnn", "Acceso correcto")
        acierta = True
        break
    else:
        msgbox("Error", "Acceso incorrecto")

if passwd_usuario != valida:
    sys.exit()
    
#if acierta == False:
#    sys.exit()
    
msgbox("Estás dentro del programa ...")
