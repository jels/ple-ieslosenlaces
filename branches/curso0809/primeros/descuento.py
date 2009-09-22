"""
Este programa calcula el porcentaje de la rebaja aplicada.
AUTOR: Jorge
"""
#Poner precios
precio = input('Introduzca el precio sin rebaja: ')
rebaja= input ('Introducir el precio con rebaja: ')
#Calcular rebaja
c1=precio-rebaja
total= c1/float(precio)*100
#resultado
print ('La rebaja aplicada es: '),total
raw_input ('Pulse intro para finalizar') 
