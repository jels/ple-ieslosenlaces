# -*- coding: cp1252 -*-

"""
Escribe un programa datos_personales.py, que pida al usuario
su nombre y apellidos y muestre el nombre con la primera letra
en may�sculas y el resto en min�sculas y el apellido todo en may�sculas,
independientemente de c�mo lo haya introducido el usuario.
"""

# toma de datos
nombre = raw_input("Introduzca el nombre: ")
apellido = raw_input("Introduzca el apellido: ")

# imprimimos modificado
print nombre.title(), apellido.upper()
