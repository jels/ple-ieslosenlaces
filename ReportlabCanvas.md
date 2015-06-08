Api de más bajo nivel, más cercano al modelo del PDF.

```
# -*- coding: utf-8 -*-

from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm, mm, inch

import os

# creación del documento. Por defecto crea un A4. Si es necesario se especifia pagesize=
pdf = Canvas("intro_reportlab.pdf")

pdf.setFont("Helvetica", 48)
pdf.setStrokeColorRGB(0, 0, 1)
pdf.drawCentredString(A4[0]/2, A4[1]-A4[1]/3, "Introducción a Reportlab")

pdf.setFont("Helvetica", 14)
pdf.setStrokeColorRGB(0, 0, 0)
pdf.drawString(inch, 5*inch, u"Reportlab es una librería de Python para crear documentos pdf")

# Introducimos líneas
definicion = pdf.beginText(inch, inch*4)
pdf.setFont("Helvetica", 12)
#   de una en una
definicion.textLine(u"PDF (acrónimo del inglés Portable Document Format, formato de documento portátil)")
definicion.textLine(u"es un formato de almacenamiento de documentos, desarrollado por la empresa")
definicion.textLine(u"Adobe Systems. Este formato es de tipo compuesto (imagen vectorial, mapa de bits y texto)")
#   varias a la vez
lineas = """
Está especialmente ideado para documentos susceptibles de ser impresos, 
ya que especifica toda la información necesaria para la presentación final
del documento, determinando todos los detalles de cómo va a quedar, no 
requiriéndose procesos anteriores de ajuste ni de maquetación. Cada vez se 
utiliza más también como especificación de visualización, gracias a la gran 
calidad de las fuentes utilizadas y a las facilidades que ofrece para el 
manejo del documento, como búsquedas, hiperenlaces, etc.
"""
definicion.textLines(lineas)

pdf.drawText(definicion)
# imagen
pdf.drawImage("http://www.reportlab.org/rsrc/rl_logo.gif", A4[0]/2, inch)

# cerramos la página actual
pdf.showPage()

# se guarda el trabajo
pdf.save()

os.system('evince intro_reportlab.pdf')
```