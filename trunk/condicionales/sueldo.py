# -*- coding: cp1252 -*-
"""
Nuestra compañía paga el 50% más por las horas extras trabajadas
durante la semana (35 horas).
Haz un programa que pida el número de horas trabajadas durante
la semana y el precio por hora y que muestre lo que hay que pagar esa semana.
"""

# captura de datos
horas = raw_input("Introduzca horas: ")
horas = int(horas)
precio = raw_input("Introduzca precio hora: ")
precio = int(precio)

# proceso

sueldo = precio * horas
if horas > 35:
    sueldo = sueldo + (horas-35) * precio * 0.5

# salida
print "Tu sueldo esta semana es de", sueldo, "€"

