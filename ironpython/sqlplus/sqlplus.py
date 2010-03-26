'''
Created on 25/03/2010

@author: lm
'''
import clr
clr.AddReference("System.Data") 
clr.AddReference("System.Data.SQLite") 
clr.AddReference("System.Xml")
clr.AddReference("PresentationFramework")
clr.AddReference("PresentationCore")

import System;
import System.Data
from System.Data import DbType, DataSet
from  System.Data.SQLite import SQLiteConnection, SQLiteDataAdapter

from System.IO import StringReader, File
from System.Xml import XmlReader
from System.Windows.Markup import XamlReader, XamlWriter
from System.Windows import Window, Application
from System.Windows.Data import Binding
from System.Windows.Controls import GridView, GridViewColumn


class MiBase(object):
    def __init__(self):
        self.fichero = r"c:\mydatabasefile.db3"
        self.cadena_con = "Data Source=%s;Version=3;"
        self.con = SQLiteConnection()
        self.carga_xaml()
        
    def carga_xaml(self):
        #file = File.OpenRead("interfaz.xaml")
        file = File.OpenRead("interfaz_con_listview.xml")
        self.win = XamlReader.Load(file)
        self.texto = self.win.FindName('consulta')
        self.boton = self.win.FindName('boton')
        self.etiqueta = self.win.FindName('label1')
        self.boton.Click += self.busca
        self.listbox = self.win.FindName('resultado')
    def crear(self):
        self.con.CreateFile(self.fichero);
    def conectar(self):
        self.con.ConnectionString = self.cadena_con % self.fichero
        self.con.Open()
    def crea_tabla(self):
        cadena = """create table productos
                (clave text, descripcion text, precio real)
                """
        command = self.con.CreateCommand()
        command.CommandText = cadena
        command.ExecuteNonQuery()
    def inserta(self):
        command = self.con.CreateCommand()
        command.CommandText = """insert into productos (clave, descripcion, precio)
                 values (:clave, :desc, :precio)"""
        valores = [['leche', 'leche pascual', '1.02'],
                   ['pan', 'pan de horno', 0.65],
                   ['yogur', 'yogur de marca', 1.20]
                   ]
        command.Parameters.Add('clave', DbType.String)
        command.Parameters.Add('desc', DbType.String)
        command.Parameters.Add('precio', DbType.Decimal)
        
        for v in valores:
            command.Parameters['clave'].Value = v[0]
            command.Parameters['desc'].Value = v[1]
            command.Parameters['precio'].Value = v[2]
            command.ExecuteNonQuery()
    def consulta(self):
        dataset = DataSet()
        adaptador = SQLiteDataAdapter()
        command = adaptador.SelectCommand = self.con.CreateCommand()
        command.CommandText ="select * from productos"
        adaptador.Fill(dataset, 'TablaProductos')
        tabla = dataset.Tables['TablaProductos']
        cols = tabla.Columns.Count
        for f in tabla.Rows:
            for c in range(cols):
                print f[c],
            print
            
    def muestra_tabla(self, tabla):
        cols = tabla.Columns.Count
        for f in tabla.Rows:
            for c in range(cols):
                print f[c],
            print
            
    def busca(self, event, args):
        self.conectar()
        dataset = DataSet()
        adaptador = SQLiteDataAdapter()
        command = adaptador.SelectCommand = self.con.CreateCommand()
        command.CommandText = self.texto.Text
        adaptador.Fill(dataset, 'TablaProductos')
        tabla = dataset.Tables['TablaProductos']
        for c in  tabla.Columns:
            print c
        self.muestra_tabla(tabla)
        
        #self.listbox.ItemsSource = tabla.Rows
        self.listbox.View = self.CreateGridViewColumns(tabla)
        self.listbox.DataContext  = dataset
        
        #print tabla.Rows
        #self.desconecta()
    def CreateGridViewColumns(self, data_table):
        """ basado en http://weblogs.asp.net/psheriff/archive/2010/03/08/using-a-wpf-listview-as-a-datagrid.aspx
        """    
        gv = GridView()
        gv.AllowsColumnReorder = True
        for col in data_table.Columns:
            gvc = GridViewColumn()
            gvc.DisplayMemberBinding = Binding(col.ColumnName)
            gvc.Header = col.ColumnName
            gvc.Width = System.Double.NaN
            gv.Columns.Add(gvc)
        return gv


miBase = MiBase()
#miBase.crear()
#miBase.conectar()
#miBase.crea_tabla()
#miBase.inserta()
#miBase.consulta()
#print "done."
Application().Run(miBase.win)
