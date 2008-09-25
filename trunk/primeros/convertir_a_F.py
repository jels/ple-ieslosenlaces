# -*- coding: cp1252 -*-

"""
Modifica el programa convertir_a_F.py para que muestre una
tabla de valores Cent�grados - Fahrenheit de 0� C a 100� C.
"""

# Programa que convierte grados C a grados Fahrenheit.
# Pide los grados al usuario, hace el c�lculo y muestra el resultado.

# Buscamos f�rmula de conversi�n: http://es.wikipedia.org/wiki/Grado_Fahrenheit
# F�rmula: F = 1.8 * C + 32


# Petici�n de entrada:
# gradosC = input("Introduce grados Cent�grados: ")
# Ahora no pedimos datos de entrada --> range(101)

for gradosC in range(101):
    # C�lculo del resultado
    gradosF = 1.8 * gradosC + 32
    # Muestra resultado
    print gradosC, '� centr�grados son', gradosF, '� Fahrenheit'

# Si ejecutamos en windows hay que parar para ver el resultado
raw_input('Pulsa intro para terminar')
