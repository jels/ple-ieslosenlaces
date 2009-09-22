# -*- encoding: utf-8 -*-

"""
Este programa pide un número de mes al usuario 
y escribe nombre del mes abreviado
Almacenamos los meses en una cadena:
Mes    Número    Posición
-------------------------
Ene      1         0
Feb      2         3
Mar      3         6
...

Las posiciones son múltiplos de 3. Para obtener la posición, 
le restamos 1 al número de mes y lo multiplicamos por 3

"""

meses = "Enero Febrero Marzo Abril Mayo Junio Julio Agosto \
Septiembre Octubre Noviembre Diciembre"

num_mes = raw_input("Introduce el número del mes: ")
num_mes = int(num_mes)

lista_meses = meses.split()


mes_abrev = lista_meses[num_mes -1]

print 'El mes número', num_mes, 'es', mes_abrev
