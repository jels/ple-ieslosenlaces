"""
Pregunta contrase�a al usuario
Si est� bien muestra mensaje de bienvenida
Si est� mal, mensaje de error

versi�n 2. contrase�a cifrada
versi�n 1. contrase�a abierta
"""

password = "programacion"

# pedir palabra al usuario
acceso = raw_input("Introduzca contrase�a: ")

if acceso == password:
    print "Acceso permitido"
else:
    print "Acceso denegado"
    
