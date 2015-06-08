**Page Layout and Typography Using Scripts**

Platypus ofrece una API de más alto nivel. Separa formato de contenido. Tiene recursos predefinidos para tablas y otras estructuras.

```
# -*- coding: utf-8 -*-

from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT, TA_RIGHT
from reportlab.lib.units import cm, mm, inch
from reportlab.lib import colors

import os

estilo = getSampleStyleSheet()

pdf = SimpleDocTemplate('Intropdf.pdf', pagesize=A4)

contenido = []

#### título
# definimos estilo para título
es_titulo = estilo['Heading1']
es_titulo.alignment=TA_CENTER
# creamos título con estilo
titulo = Paragraph("Introducción a PDF", es_titulo)
contenido.append(titulo)

# espacio adicional
contenido.append(Spacer(0, inch*.1))

                 
texto = "PDF (acrónimo del inglés Portable Document Format, formato de documento portátil) \
es un formato de almacenamiento de documentos, desarrollado por \
la empresa Adobe Systems. Este formato es de tipo compuesto \
(imagen vectorial, mapa de bits y texto)"
para = Paragraph(texto, estilo['Normal'])
contenido.append(para)

# espacio adicional
contenido.append(Spacer(0, inch*.2))

# tabla
datos = (
    ('Nombre ciclo', 'Núm. Alumnos', 'Núm aprobados'),
    ('Desarrollo Aplic. Informáticas', 15, 5),
    ('Admin. Sist. Informáticos', 40, 25),
    ('Explotación Sist. Informáticos', 50, 20)
    )
tabla = Table(data = datos,
              style = [('GRID',(0,0),(-1,-1),0.5,colors.grey),
                       ('BOX',(0,0),(-1,-1),2,colors.black),
                       ('BACKGROUND', (0, 0), (-1, 0), colors.pink),
                       ]
              )

contenido.append(tabla)

# espacio adicional
contenido.append(Spacer(0, inch*.4))


para2 = Paragraph(u"""Gráficos de ejemplo de <a href="http://www.reportlab.org/meteo.html" color="blue">
reportlab.org</a>""", style=estilo['Normal'])
contenido.append(para2)
contenido.append(Spacer(0, inch*.1))

# imagen
foto = Image("http://www.reportlab.org/rsrc/meteo.gif")
# Ajustamos tamaño al ancho porque es más grande
ancho = A4[0]-2*inch
foto.drawHeight = ancho * foto.drawHeight/foto.drawWidth
foto.drawWidth = ancho

contenido.append(foto)

pdf.build(contenido)

os.system('evince Intropdf.pdf')
```