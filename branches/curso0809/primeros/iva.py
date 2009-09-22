"""
Este programa calcula el iva sobre el precio que se pongo.
AUTOR: Jorge
"""
#Poner precio
precio = input('Introduzca el precio sin iva: ')
#Calcular iva
iva = precio *0.16
total= iva+precio
#resultado
print ('El precio con iva es: '),total
raw_input ('Pulse intro para finalizar') 
