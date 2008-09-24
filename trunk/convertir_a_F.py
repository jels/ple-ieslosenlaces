# -*- coding: utf-8 -*-

# Programa que convierte grados C a grados Fahrenheit.
# Pide los grados al usuario, hace el cálculo y muestra el resultado.

# Buscamos fórmula de conversión: http://es.wikipedia.org/wiki/Grado_Fahrenheit
# Fórmula: F = 1.8 * C + 32

# Petición de entrada:
gradosC = input("Introduce grados Centígrados: ")

# Cálculo del resultado
gradosF = 1.8 * gradosC + 32

# Muestra resultado
print gradosC, 'º centrígrados son', gradosF, 'º Fahrenheit'

# Si ejecutamos en windows hay que parar para ver el resultado
raw_input('Pulsa intro para terminar')
