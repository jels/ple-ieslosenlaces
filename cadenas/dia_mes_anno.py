# -*- encoding: utf-8 -*-

"""
Conversor de fechas
convierte fechas en el formato "dd/mm/aaaa" a "dia de mes de año"
"""

# Toma de datos de la fecha
fecha_cadena = raw_input("Introduce la fecha (dd/mm/aaaa): ")
dia, mes, anno = fecha_cadena.split('/')

# Meses ***** Por terminar ****
meses = ["Enero", "Febrero", "Marzo", "..."]

mes_cadena = meses[int(mes)-1]

print "%s de %s de %s" % (dia, mes_cadena, anno)