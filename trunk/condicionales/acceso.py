# -*- coding: cp1252 -*-
"""
Ejercicio con contrase�as
"""

from easygui import *
import sys

# password v�lida
valida = "megustapython"


# pedir datos 5 veces como m�ximo
# centinela
acierta = False
for x in range(5):
    passwd_usuario = passwordbox("Introduzca su contrase�a", "Control de acceso")

    # comprobaciones
    # cancelaci�n
    if passwd_usuario == None:
        msgbox("Operaci�n cancelada")
        sys.exit()
    # v�lidar
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
    
msgbox("Est�s dentro del programa ...")
