import os

def ruta(archivo):
    return os.path.join(os.path.dirname('.'), archivo)

print ruta('hola')


