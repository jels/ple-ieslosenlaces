# -*- encoding: utf-8 -*-

from graphics import *

#Creamos la ventana
ventana = GraphWin('Conversor de temperaturas',800,600)
ventana.setBackground('white')

#Introduccion al programa
Text(Point(400,20),'Bienvenido al convertidor de temperaturas.').draw(ventana)
Text(Point(400,40),'Este programa pasara de Fº a Cº').draw(ventana)

#Pedir grados farenheit
Text(Point(400,100),'Introduzca la temperatura en Fº').draw(ventana)
gradosF = Entry(Point(400,150),5)
gradosF.draw(ventana)

Text(Point(400,200),'Despues de introducir los grados haga click').draw(ventana)
ventana.getMouse()

#Convertir a Centigrados
gradosF = float(gradosF.getText())
gradosC = (gradosF-32)/1.8

#Mostrar resultado
Text(Point(400,300),'%.2f grados Farenheit son %.2f grados C'%(gradosF,gradosC)).draw(ventana)


Text(Point(400,500),'Haga click para salir').draw(ventana)
ventana.getMouse()
ventana.close()