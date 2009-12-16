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
        self.lista_amigos = []
    def pon_amigo(self, amigo):
        self.lista_amigos.append(amigo)
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
        
    
if __name__ == '__main__':
    import pprint
    amigo1 = Amigo('Pedro', 'Vidal')
    amigo2 = Amigo('Ana', 'Pérez')
    amigo3 = Amigo('Pedro', 'Pérez')
    amigo1.pon_telefono(666777888)
    amigo1.pon_telefono('976-123-456')
    amigo1.pon_correo('pedro@hotmail.com')
    amigo1.pon_correo('pedro@gmail.com')
    agenda = Agenda()
    agenda.pon_amigo(amigo1)
    agenda.pon_amigo(amigo2)
    agenda.pon_amigo(amigo3)
    agenda.listado()
    print 'Tengo', agenda.num_contactos(), 'contactos.'
    # recorro los resultados de .buscar
    for am  in  agenda.buscar('peDRo'):
        print am
    for am in agenda.buscar(apellido='pérez'):
        print am