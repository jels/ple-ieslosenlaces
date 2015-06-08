
```
# -*- coding: utf-8 -*-

import cairo
import pycha.bar

# creación de la plantilla
ancho, alto = (400,200)
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, ancho, alto)

# datos agrupados
data_set = (
    (u'Programación', ((0,2), (1, 4), (2, 3), (3, 2))),
    (u'Análisis', ((0, 4), (1, 3), (2, 1), (3, 2))),
    (u'Sistemas', ((0,1), (1, 5), (2, 4), (3, 1)))
)

# configuración opciones del gráfico
options = {
    'legend': {'hide': False,
               'position': {'right': 20}
               },
    'background': {'chartColor': '#444444',
                   'baseColor': '#FFFFFF'},
    'colorScheme': 'blue',
    'axis': {
            'x': {
                'ticks': ({'label': u'Insuf.', 'v': 0},
                          {'label': u'Aprobado', 'v': 1},
                          {'label': u'Notable', 'v': 2},
                          {'label': u'Sobres.', 'v': 3},
                          ),
                'label': 'Notas',
                #'rotate': 25,
            },
            'y': {
                'tickCount': 6,
                'label': u'Núm.'}
            }
    }

# generación del gráfico
grafico = pycha.bar.VerticalBarChart(surface, options)
grafico.addDataset(data_set)
grafico.render()

surface.write_to_png('notas.png')
```