import random

class Conductor(object):
    def __init__(self, nombre, permiso):
        self.__nombre = nombre
        self.__permiso = permiso
    def get_nombre(self):
        return self.__nombre
    def get_permiso(self):
        return self.__permiso
    def __str__(self):
        return "%s [%s]" % (self.__nombre, self.__permiso)
        

class Camion(object):
    def __init__(self, matricula, peso_max):
        self.matricula = matricula
        self.peso_max = peso_max
        self.__carga = 0
    def __str__(self):
        return "%s :: %d (%d)" % (
            self.matricula,
            self.peso_max,
            self.__carga)
    def cargar(self, peso):
        """
        Carga un peso en el camión. Si supera el máximo, devuelve
        lo que sobra. Si no, devuelve 0
        """
        aux  = self.__carga + peso
        if aux > self.peso_max:
            self.__carga = self.peso_max
            return aux - self.peso_max  # devolvemos lo que no se ha podido cargar
        else:
            self.__carga = self.__carga + peso
            return 0

    def descargar(self, peso):
        """
        Falta comprobar míximo
        """
        aux  = self.__carga - peso
        if aux < 0:
            self.__carga = 0
            return abs(aux)
        else:
            self.__carga = aux
            return 0

    def peso(self):
        return self.__carga
    def set_conductor(self, conductor):
        self.conductor = conductor
    def get_conductor(self):
        return self.conductor
    def __cmp__(self, otro):
        return cmp(self.__carga, otro.__carga)

    

        

