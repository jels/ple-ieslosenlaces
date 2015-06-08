
```
# -*- coding: utf-8 -*-

import cairo
import pycha.pie

# creación de la plantilla
ancho, alto = (400,200)
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, ancho, alto)

# datos agrupados
data_set = [(u'Suficiente', ((0,2),)),
            (u'Aprobado', ((1, 4),),),
            (u'Notable', ((2, 3),),),
            (u'Sobresaliente', ((3, 2),),),]

options = {
    'legend': {'hide':True},
    'background': {'color': '#F0F0F0'},
    'title': u'Notas de programación'
    }

grafico = pycha.pie.PieChart(surface, options)
grafico.addDataset(data_set)
grafico.render()

surface.write_to_png('notas_sectores.png')




```