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
        

        
#1. crea lista de camiones
lista_camiones = []
for x in range(10):
    pesos = [5000, 10000, 20000]
    c = Camion("%04dXXX" % x , random.choice(pesos))
    lista_camiones.append(c)
for cam in lista_camiones:
    print cam

print '*' * 10

#2. Pone pesos entre 1000 y 10000
for cam in lista_camiones:
    sobra = cam.cargar(random.randint(1000, 10000))
    if sobra > 0:
        print 'No puedo cargar', sobra, 'en camion', cam

#3. Crear conductores
conductores = "Juan Pedro Marta Ana Pilar Miguel Pablo María Carmen Javier"
lista_conductores = []
for nombre in conductores.split():
    lista_conductores.append(Conductor(nombre, 'C1::' +str(random.randrange(10, 100))))

for c in lista_conductores:
    print c
print '*' * 10

# asigna conductor a camión
for cam, con in zip(lista_camiones, lista_conductores):
    cam.set_conductor(con)
    
# imprime conductores
for cam in lista_camiones:
    conductor = cam.get_conductor()
    print conductor
    
    
"""    
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
    

    
        
        
    
"""
