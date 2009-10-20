from easygui import *

mensaje_largo = """Estamos buscando jugadoras para nuestro equipo

Introduce sexo m/f
"""

sexo = enterbox(mensaje_largo, "Captura de datos")

if sexo.lower() == 'f':
    edad = enterbox("Introduce edad", "Captura de datos")
    if edad >= 18 and edad <=22:



    
"""
INCOMPLETO
"""
