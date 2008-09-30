# -*- coding: cp1252 -*-



'''
Crea un programa hipoteca.py
que pida la cantidad dinero del pr�stamo,
la TAE y los a�os en que vas a devolver el pr�stamo.
El programa mostrar� la cuota mensual del mismo.
Ver ejemplo de c�lculo en
http://es.wikipedia.org
Aqu� tienes un simulador para comprobar tus datos
http://www.calculodehipoteca.net/simuladores/amortizacion-2/

AUTOR: PABLO MARTIN
VERSION: 1.0
'''

#Introduccion al programa
print ' Hola, con este programa calcularemos la cuota mensual de una hipoteca '
print '*'*80

#Entrada de datos
capital = float (input (' Introduzca la cantidad que va a pedir: '))
anos = input (' Introduzca los a�os en los que desea pagar el prestamo: ')
interes = float (input (' Introduzca el T.A.E que le aplica el banco: '))

#Operaciones necesarias
plazos = anos * 12
interesMensual = interes / 12

cuota = capital*interesMensual/(100*(1-(1+interesMensual/100)**-plazos))
round (cuota, 2)

hipoteca = cuota * plazos
                                    
#Mostrar resultado
print ' En una hipoteca de capital: ', capital, ' y con un interes de ', interes
print ' a pagar en: ', anos, ' a�os '
print ' Tendra que pagar ', plazos, ' cuotas mensuales de ', cuota, ' euros '
print ' Con lo que usted debera pagar un total de: ', hipoteca

#Fin
raw_input (' Pulse inro para salir ')
