# -*- encoding: utf-8 -*-

'''
Ejemplo de uso de SQLAlchemy con la base de datos MySql: world
El programa usa jython con zxJDBC.

Requisitos: conector de mysql

lm
'''

from sqlalchemy import *
from sqlalchemy.orm import sessionmaker, mapper, relationship, backref

# 1. Definición del motor de base de datos que vamos a usar con sqlalchemy:
# La estructura de la cadena es:
#      dialect+driver://username:password@host:port/database
bdatos = create_engine('mysql+zxjdbc://dai:dai@localhost/world')

# 2. Con MetaData accedemos a la colección de tablas y sus esquemas asociados
metadata = MetaData(bdatos)

# 3. Creamos las tablas internas (de sqlalchemy)
#    con los metadatos extraídos de la base de datos.
tabla_paises = Table('country', metadata, autoload=True)
tabla_ciudades = Table('city', metadata, 
                       Column('CountryCode', ForeignKey('country.Code')),
                       autoload=True 
                       )
# 4. Creamos los objetos con los que vamos a acceder a los datos.
#    Declaramos las clases vacías para que se rellenen con los metadatos
#    extraídos de la base de datos.
class Pais(object):
    pass
class Ciudad(object):
    pass

# 5. Relacionamos nuestros objetos con las tablas de la Base de Datos
#    Añadimos la relación Ciudad / Pais
paismapper = mapper(Pais, tabla_paises,
                    properties = {'ciudades' : relationship(Ciudad, backref='pais')}
                    )
ciudadmapper = mapper(Ciudad, tabla_ciudades)

# 6. Creación de una sesión sobre la conexión de base de 
#    datos configurada antes.
Session = sessionmaker(bind = bdatos)
sesion = Session()

# 7. Sobre el objeto sesión creado podemos hacer las consultas

# 7.1 Consulta simple: Todos los países. La consulta devuelve una
#     secuencia de países. Recorremos la lista de países recuperada
#     e imprimimos su columna 'Name'
for pais in sesion.query(Pais).all():
    print pais.Name

print '*' * 40

# 7.2 Consuta sencilla: Seleccionamos España y depués aprovechamos la
#     propiedad creada (clave foránea de ciudad) para imprimir las
#     ciudades de España que tengan más de 500000 habitantes (campo 
#     Population 
for pais in sesion.query(Pais).filter(Pais.Name == 'Spain'):
    for ciudad in  pais.ciudades:
        if ciudad.Population > 500000:
            print ciudad.Name, ciudad.pais.Name

print '*' * 40

# 7.3 Consulta filtrando un campo y ordenando resultado.
#     Se aprovecha la relación para imprimir el nombre del país de
#     cada ciudad seleccionada.       
for ciudad in sesion.query(Ciudad).filter(Ciudad.Population > 1000000).order_by(Ciudad.Population):
    print "%-20.18s %-20.18s %10d" % ( ciudad.Name, ciudad.pais.Name, ciudad.Population)