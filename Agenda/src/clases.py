# -*- encoding: utf-8 -*-
'''
Created on 16/12/2009

@author: lm
'''

class Amigo(object):
    '''
    Amigo: clase para almacenar información 
    de nuestros amigos
    Atributos:
    * nombre
    * apellido
    * telefonos
    * correos
    '''

    def __init__(self, nombre, ape):
        '''
        Constructor. Inicializa nombre y apellido
        '''
        # almaceno las cadenas como unicode
        # para evitar problemas con los acentos
        self.nombre = unicode(nombre)
        self.apellido = unicode(ape)
        self.telefonos = []
        self.correos = []
    def pon_telefono(self, telefono):
        '''
        Añade teléfono a la lista de telfs ...
        telefono --> str
        '''
        telefono = str(telefono)
        telefono = telefono.replace('-', '')
        self.telefonos.append(telefono)
    def pon_correo(self, correo):
        self.correos.append(correo)
        
    def __str__(self):
        return """%s %s \n%s \n%s""" %  (
                                         self.nombre, 
                                         self.apellido.upper(),
                                         '; '.join(self.telefonos),
                                         '; '.join(self.correos) 
                                         )
class Agenda(object):
    def __init__ (self):
        self.fichero = "miagenda.csv"
        self.lista_amigos = []
    def pon_amigo(self, amigo):
        self.lista_amigos.append(amigo)
    def quita_amigo(self, amigo):
        self.lista_amigos.remove(amigo)

    def listado(self):
        for n, amigo in enumerate(self.lista_amigos):
            print n+1, amigo
            print
    def num_contactos(self):
        '''num_contactos() --> devuelve entero
        '''
        return len(self.lista_amigos)
    
    def buscar(self, nombre= "", apellido=""):
        '''
        Devuelve objeto Amigo. Si no existe, 

        Puede haber más de uno: devuelve lista
        '''
        encontrado = []
        nombre = nombre.lower()
        apellido = apellido.lower()
        for am in self.lista_amigos:
            if am.nombre.lower() == nombre or  \
                        am.apellido.lower() == apellido:
                encontrado.append(am)
        return encontrado
    def guardar(self):
        '''
        Almacena los datos de la agenda en un fichero csv
        '''
        # Abrir fichero escritura
        f = open(self.fichero, 'w')
        # Recorrer lista_amigos
        for am in self.lista_amigos:
            # Para cada amigo: guardar sus datos en 
            # una línea, separados por un ';'
            # ej datos: ['Pepe', 'Pérez','123, 456', 'p@com, j@com']
            datos=[am.nombre, am.apellido, 
                   ','.join(am.telefonos),
                   ','.join(am.correos)]
            f.write(';'.join(datos)+'\n')
        f.close()
        
    def cargar(self):
        '''
        Carga los datos de un fichero .csv a la agenda
        '''
        # abre fichero lectura
        f = open(self.fichero)
        # recorre línea a línea
        for linea in f:  
            # split ; --> 4 elementos
            n, ap, lt, lc = linea.strip().split(';')  # nombre, ape, lista tel, lista correos             
            # [0] --> nombre
            # [1] --> apellido
            # [2] --> lista de telfs separados por ','
            # [3] --> lista de correos separados por ','
            # Crear amigo --> Amigo(nombre, ape)
            amigo = Amigo(n, ap)
            # Añadir telfs  (split , )
            for tel in lt.split(','):
                amigo.pon_telefono(tel)
            # Añadir correos (split ,)
            for cor in lc.split(','):
                amigo.pon_correo(cor)
            # Añadir amigo a lista_amigos
            self.lista_amigos.append(amigo)
        f.close()
    
if __name__ == '__main__':
    agenda = Agenda()
    agenda.cargar()
    agenda.listado()
    encontrado = agenda.buscar(apellido='Pérez')
    agenda.quita_amigo(encontrado) # encontrado es una lista
    agenda.listado()
    agenda.guardar()
    
    