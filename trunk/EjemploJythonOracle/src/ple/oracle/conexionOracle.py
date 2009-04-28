#-*- encoding: utf-8 -*-

'''
Created on 28/05/2009

@author: lm
'''

from oracle.jdbc.driver import OracleDriver
from java.sql import *

class Conexion:
    def __init__(self):
        self.usuario = 'dai1'
        self.passw = 'tiger'
        self.host = '172.30.6.190'
        self.puerto = '1521'
        self.sid = 'ENLACES5'
        self.url = "jdbc:oracle:thin:@%s:%s:%s" % (self.host,
                                                   self.puerto,
                                                   self.sid)
    def conectar(self):
        driver = OracleDriver()
        DriverManager.registerDriver(driver)
        self.conexion = DriverManager.getConnection(self.url, self.usuario, 
                                               self.passw)
    def desconectar(self):
        self.conexion.close()
        
    def banner(self):
        self.conectar()
        sentencia = self.conexion.createStatement()
        rset = sentencia.executeQuery("SELECT banner FROM sys.v_$version")
        while (rset.next()):
            print rset.getString(1)
        sentencia.close()
        self.desconectar()
        
    def creaEmpleados(self):
        crea_tabla = """create table Employees (Employee_ID INTEGER, 
                               Name VARCHAR(30))"""
        self.conectar()
        sentencia = self.conexion.createStatement()
        sentencia.executeUpdate(crea_tabla)
        sentencia.close()
        self.conexion.close()
           
        
if __name__ == '__main__':
    miCon = Conexion()
    miCon.banner()
    miCon.creaEmpleados()
        
        
        
        
        
        
        
        
        
        
        

