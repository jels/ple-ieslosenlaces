
```
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.graphics.barcode import code39

c = canvas.Canvas("barcode.pdf", pagesize = A4)
barcode=code39.Extended39("123456789",barWidth=0.5*mm,barHeight=20*mm)
barcode.drawOn(c,100*mm,100*mm)
c.showPage()
c.save()
```