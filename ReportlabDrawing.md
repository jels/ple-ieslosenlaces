# Ejemplo de un gráfico con Drawing #
```
# -*- coding: utf-8 -*-

from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import cm, mm, inch
from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.linecharts import HorizontalLineChart
from reportlab.graphics.widgets.markers import makeMarker

import os

estilo = getSampleStyleSheet()

pdf = SimpleDocTemplate('Calificaciones.pdf', pagesize=A4)

contenido = []

#### título
# definimos estilo para título
es_titulo = estilo['Heading1']
es_titulo.alignment=TA_CENTER
# creamos título con estilo
titulo = Paragraph("Calificaciones Informática", es_titulo)
contenido.append(titulo)

# espacio adicional
contenido.append(Spacer(0, inch*.1))


drawing = Drawing(400, 200)
lc = HorizontalLineChart()
lc.x = 30
lc.y = 50
lc.height = 125
lc.width = 350
lc.data = [[8,10,5,2]]
lc.categoryAxis.categoryNames = ['Suspenso', 'Aprobado', 'Notable', 'Sobresaliente']
lc.categoryAxis.labels.boxAnchor = 'n'
lc.valueAxis.valueMin = 0
lc.valueAxis.valueMax = 12
lc.valueAxis.valueStep = 2
lc.lines[0].strokeWidth = 2
lc.lines[0].symbol = makeMarker('FilledCircle') # círculos rellenos
lc.lines[1].strokeWidth = 1.5
drawing.add(lc)

contenido.append(drawing)

pdf.build(contenido)

os.system('evince Calificaciones.pdf')
```