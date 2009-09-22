# -*- coding: cp1252 -*-



'''
Sensación térmica es la acción combinada de frío y viento.
Dada una temperatura en grados C y la velocidad del viento (en km/hora),
calcula la Temperatura aparente (windchill).
Busca en internet la fórmula. Aquí tienes una:
http://es.wikipedia.org/wiki/Temperatura_de_sensaci%C3%B3n.

Escribe un programa sensacion_termica.py
que pida los datos necesarios, haga las conversiones oportunas,
calcule el resultado y lo muestre al usuario.
Documenta el programa correctamente.


AUTOR: PABLO MARTIN

'''


#Introduccion al programa
print 'Hola, este progra calculara la sensacion termica '.center(80)
print '*'*80
print '*'*80


#Entrada de datos necesarios para calcular la temperatura de sensacion
temperatura = input('Introduzca la temperatura en Cº: ')
viento = input('Introduzca la velocidad del viento en Km/h: ')


#Usando los datos que tenemos, calculamos la temperatura de sensacion
#S=13.12+0.6215*t-11.37*v**0.16+0.3965*t*v**0.16

t_sensacion = 13.12 + 0.6215*temperatura - 11.37*viento**0.16 + \
              0.3965*temperatura*viento**0.16

#Mostrar resultado

print 'Con una temperatura de', temperatura, 'Cº',\
      'y un viento de', viento, 'Km/h', 'La sensacion termica sera de',\
      round(t_sensacion,2), 'Cº'

print 'Con una temperatura de %.2f Cº \
y un viento de %.2f  La sensacion termica sera de %.2fºC' % (temperatura,
                                                                  viento,
                                                                  t_sensacion)

#Fin
raw_input('Pulse intro para salir'.center(80))
