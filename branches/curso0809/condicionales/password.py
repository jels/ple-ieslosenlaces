"""
Pregunta contraseña al usuario
Si está bien muestra mensaje de bienvenida
Si está mal, mensaje de error

versión 2. contraseña cifrada
versión 1. contraseña abierta
"""

password = "programacion"

# pedir palabra al usuario
acceso = raw_input("Introduzca contraseña: ")

if acceso == password:
    print "Acceso permitido"
else:
    print "Acceso denegado"
    
