"""
Este programa aplica la rebaja al precio indicado.
AUTOR: Jorge
"""
#Poner precio
precio = input('Introduzca el precio sin rebaja: ')
rebaja= input ('Introducir porcentaje de rebaja: ')
#Calcular rebaja
rbj= precio*(rebaja/100.)
total=precio-rbj
#resultado
print ('El precio del producto rebajado es: '),total
raw_input ('Pulse intro para finalizar') 
