
# Ejemplo #
```
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
        self.conexion = None
    def conectar(self):
        try:
            driver = OracleDriver()
            DriverManager.registerDriver(driver)
            self.conexion = DriverManager.getConnection(self.url, self.usuario, 
                                               self.passw)
        except:
            print "Error en la conexion"
            
    def desconectar(self):
        try:
            self.conexion.close()
        except: 
            print "Error al desconectar"
        
    def banner(self):
        self.conectar()
        sentencia = self.conexion.createStatement()
        rset = sentencia.executeQuery("SELECT banner FROM sys.v_$version")
        while (rset.next()):
            print rset.getString(1)
        sentencia.close()
        self.desconectar()
        
    def creaEmpleados(self):
        crea_tabla = """create table Empleados (Empleado_ID INTEGER, 
                               Nombre VARCHAR(30))"""
        self.conectar()
        sentencia = self.conexion.createStatement()
        sentencia.executeUpdate(crea_tabla)
        sentencia.close()
        self.desconectar()

       
if __name__ == '__main__':
    miCon = Conexion()
    miCon.banner()
    miCon.creaEmpleados()
       
```


# Otro ejemplo #
www.oracle.com/technology/products/oracle-data-integrator/10.1.3/htdocs/documentation/oracledi\_jython\_reference.pdf
```
import java.sql as sql
import java.lang as lang
def main():
  driver, url, user, passwd = (
    'oracle.jdbc.driver.OracleDriver',
    'jdbc:oracle:thin:@172.30.6.190:1521:enlaces5',
    'dai1',
    'tiger')
  ##### Register Driver
  lang.Class.forName(driver)
  ##### Create a Connection Object
  myCon = sql.DriverManager.getConnection(url, user, passwd)
  f = open('/home/lm/jdbc_res.txt', 'w')
  try:
    ##### Create a Statement
    myStmt = myCon.createStatement()
    ##### Run a Select Query and get a Result Set
    myRs = myStmt.executeQuery("select TABLE_NAME, OWNER from ALL_TABLES where TABLE_NAME like 'SNP%'")
    ##### Loop over the Result Set and print the result in a file
    while (myRs.next()):
      print >> f , "%s\t%s" %(myRs.getString("TABLE_NAME"), myRs.getString("OWNER") )
  finally:
    myCon.close()
    f.close()

### Entry Point of the program
if __name__ == '__main__':
  main()
```