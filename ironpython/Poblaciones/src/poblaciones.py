'''
Created on 06/04/2010

@author: dai
'''
import clr
import sys
import codecs
try:
    clr.AddReference("MySql.Data")
    from MySql.Data import MySqlClient 
except:
    print "Es necesario instalar el driver de MySQL"
    sys.exit(0)

class Poblacion(object):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
        cadena_conexion = "Server=172.30.6.16;Database=poblacion;Uid=dai;Pwd=dai;"
        self.conexion = MySqlClient.MySqlConnection(cadena_conexion)
    def inicializa(self):
        self.__crea_tablas()
        self.__inserta_comunidades()
        
    def __crea_tablas(self):
        self.conexion.Open()
        instruccion = self.conexion.CreateCommand()
        f = open('crear.txt')
        tabla1, tabla2 = f.read().split('\n\n') #instrucciones
        try:
            instruccion.CommandText = "Drop table comunidad"
            instruccion.ExecuteNonQuery()
            instruccion.CommandText = tabla1  # comunidades
            instruccion.ExecuteNonQuery()
        except EnvironmentError, e:
            print "Tabla existe"
        try:
            instruccion.CommandText = tabla2  # poblaciones
            instruccion.ExecuteNonQuery()
        except EnvironmentError, e:
            print "Tabla existe"
        
        self.conexion.Close()
    def __inserta_comunidades(self):
        self.conexion.Open()
        instruccion = self.conexion.CreateCommand()
        f = codecs.open('datos_comunidades.txt')
        ca_id = MySqlClient.MySqlParameter()
        nom = MySqlClient.MySqlParameter()
        
        instruccion.CommandText = "insert into comunidad  values(@id, '@nombre')"
        instruccion.Parameters.AddWithValue('id', None)
        instruccion.Parameters.AddWithValue('nombre', None)
        
        for linea in f:
            if ',' in linea:
                ca_id, nombre = linea.split(',')
                print ca_id, nombre
                instruccion.Parameters['id'].Value =  ca_id
                instruccion.Parameters['nombre'].Value = nombre
                instruccion.ExecuteNonQuery()
        f.close()
        self.conexion.Close()
        

        
        
        
        