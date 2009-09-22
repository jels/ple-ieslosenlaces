import random

class Camion(object):
    def __init__(self, matricula, peso_max):
        self.matricula = matricula
        self.peso_max = peso_max
        self.__carga = 0
        self.conductor = ""
    def __str__(self):
        return "%s :: %d (%d)" % (
            self.matricula,
            self.peso_max,
            self.__carga)
    def cargar(self, peso):
        """
        Falta comprobar máximo
        """
        self.__carga = self.__carga + peso

    def descargar(self, peso):
        """
        Falta comprobar míximo
        """
        self.__carga = self.__carga - peso
    def peso(self):
        return self.__carga
        
        
# crea lista de camiones
lista_camiones = []
for x in range(10):
    pesos = [5000, 10000, 20000]
    c = Camion("%04dXXX" % x , random.choice(pesos))
    lista_camiones.append(c)

conductores = "Juan Pedro Marta Ana Pilar Miguel Pablo María Carmen Javier"
# con zip
for nombre, camion  in zip(conductores.split(), lista_camiones):
    camion.conductor = nombre
# con range
for x in range(10):
    lista_camiones[x].conductor = conductores.split()[x]
    
    

for cam in lista_camiones:
    print cam

def muestra_matriculas(lista):
    for num, camion in enumerate(lista):
        print "%3d ::" %(num+1), camion.matricula
# uso de muestra_matricula
print "muestra_matriculas"
muestra_matriculas(lista_camiones)


def imprime_conductores(lista):
    lista_conductores = []
    for cam in lista:
        lista_conductores.append(cam.conductor)
    lista_conductores.sort(reverse=True)
    for conductor in lista_conductores:
        print conductor
        
print "*** Imprime_conductores ***"
imprime_conductores(lista_camiones)
    

    
        
        
    
