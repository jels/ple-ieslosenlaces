# -*- encoding: utf-8 -*-
'''
Ejemplo: MySql con zxJDBC y swing usando JTable

Sobre ejemplo de Greg Moore en 
http://wiki.python.org/jython/SwingExamples#JTable

@author: lm
'''
from javax.swing import *
from javax.swing.table import DefaultTableModel
from java.awt import *
from com.ziclix.python.sql import zxJDBC

class Paises:
    ''' Clase que crea una interfaz con swing
    y muestra el resultado de una consulta con zxJDBC
    en un JPanel
    '''
    def __init__(self):
        frame = JFrame(u"Países de Europa")
        frame.setSize(350, 450)
        frame.setLayout(BorderLayout())
    
        self.tableData = self.consulta_paises()
        colNames = (u'Código', 'Nombre')
        dataModel = DefaultTableModel(self.tableData, colNames)
        self.table = JTable(dataModel)
    
        scrollPane = JScrollPane()
        scrollPane.setPreferredSize(Dimension(300,400))
        scrollPane.getViewport().setView((self.table))
    
        panel = JPanel()
        panel.add(scrollPane)
    
        frame.add(panel, BorderLayout.CENTER)
        frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE)
        frame.setVisible(True)
        
    def consulta_paises(self):
        '''método que realiza una conexión a la base de datos
        y devuelve la lista de tuplas código, país de los países
        de Europa
        '''
        bdatos = 'jdbc:mysql://localhost/mundo'   
        driver = 'com.mysql.jdbc.Driver'
        conexion = zxJDBC.connect(bdatos, 'dai', 'dai', driver)
        cursor = conexion.cursor()
        cursor.execute("""select Code, Name from country
                        where Continent = "Europe"
                        order by Name
                        """)
        return cursor.fetchall()
       

if __name__ == '__main__':
    Paises()
