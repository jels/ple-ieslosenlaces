# -*- encoding: utf-8 -*-
'''
Ejemplo interfaz compleja
Hay que añadir jar de 
http://java.sun.com/docs/books/tutorial/uiswing/examples/layout/SpringGridProject/src/layout/SpringUtilities.java
'''

from javax.swing import *
from java.awt import *
import sys
# Para SpringUtilities: dónde tenemos el .jar ?
ruta = r'E:\Utilidades\Utils.jar'
sys.path.append(ruta)
import SpringUtilities

class Interfaz(object):
    def __init__(self):
        self.frame = JFrame("Ejercicio de test")
        self.frame.layout = BorderLayout()
        self.crea_panel_datos()
        self.crea_botones()
        self.frame.pack()
        self.frame.visible = True
    def crea_panel_datos(self):
        pdatos = JPanel(SpringLayout())  # crea panel
        # widgets: 
        luser = JLabel('Usuario: ', JLabel.TRAILING)
        self.tuser = JTextField(10)
        luser.setLabelFor(self.tuser)
        pdatos.add(luser) #
        pdatos.add(self.tuser) #
        lpass = JLabel(u'Contraseña: ', JLabel.TRAILING)
        self.tpass = JPasswordField(10)
        lpass.setLabelFor(self.tpass)
        pdatos.add(lpass) #
        pdatos.add(self.tpass) #
        
        SpringUtilities.makeCompactGrid(pdatos,
                                       2, 2,
                                       6, 16,
                                       6, 16)
        self.frame.add(pdatos, BorderLayout.CENTER)
        
        
        
    def crea_botones(self):
        botones = JPanel()
        #print botones.layout
        self.bok = JButton('Aceptar')
        self.bcancel = JButton('Cancelar')
        self.botro = JButton('Otro')
        botones.add(self.bok)
        botones.add(self.bcancel)
        botones.add(self.botro)
        self.frame.add(botones, BorderLayout.SOUTH)

if __name__ == '__main__':
    Interfaz()