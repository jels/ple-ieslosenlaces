
# ADO .NET #
  * http://es.wikipedia.org/wiki/ADO.NET
  * Conectarse a datos: http://msdn.microsoft.com/es-es/library/ms171886.aspx
  * http://www.scribd.com/doc/289168/Sesion-05-ADONet

  * http://www.connectionstrings.com

# Clases principales en un proveedor de datos #
```
Connection
Command
DataReader
DataAdapter
```

# Ejemplo Postgresql #
```
import clr
clr.AddReference('Npgsql')
import Npgsql as pgslql

connection = pgsql.NpgsqlConnection('server=localhost; database=miBase; user id=postgres; password=1234')

connection.Open()

command = connection.CreateCommand()
command.CommandText = "insert into person (name) values ('Pepe Pérez')"
command.ExecuteNonQuery()

command.CommandText("select name from person where id = 1")
command.ExecuteScalar()

command.CommandText("select name from person")
lector = command.ExecuteReader()
lector.HasRows
lector.FieldCount

while lector.Read():
    print lector['id'], lector['name']


from System.Data import DataSet

dataset = DataSet()
adapter = pgsql.NpgsqlDataAdapter()

```
# Inyección de código #
Mucho cuidado con el paso de parámetros. Hay que evitar **SQL injection**.

```
# PROHIBIDO HACER ESTO
usuarios = ['Ana', 'María', 'Juan']
sentencia_insert = "insert into agenda (nombre) values ('%s')"
for u in usuarios:
    command.CommandText = sentencia_insert % u
    command.ExecuteNonQuery()
      

```
Imaginad que nos colocan como usuario `"); DROP TABLE presupuestos CASCADE;"`
## Uso de parámetros ##
Por seguridad, eficiencia,
```
command = conexion.CreateCommand()
command.CommandText = 'insert into agenda (nombre) values (:nombre)'
for u in usuarios:
    command.Parameters['nombre'].Value = u
    command.ExecuteNonQuery()
```
# Búsquedas #
## Un solo valor ##
```
>>> command.CommandText = "select count(*) from agenda"
>>> command.ExecuteScalar()
10L
>>> command.CommandText = "select nombre from agenda where id=1"
'Carmen'
```
Si la consulta devuelve varios valores, ExecuteScalar sólo devuelve el primero.
## Varios valores ##
Para recuperar varios valores necesitamos un **DataReader**
```
>>> reader = command.ExecuteReader()
```
Ver ejemplo en AdoOracle

## Transacciones ##
Propiedades transacción: **ACID**:
  * Atomicidad: todo o nada
  * Consistencia: No se puede dejar la BD en un estado inconsistente
  * 'Isolation': Otras transacciones no pueden ver los cambios de esta transacción hasta que no se hayan confirmado
  * Durabilidad: Una vez confirmada, los cambios se aplicarán incluso ante fallos del sistema.

```
transaccion = conexion.BeginTransaction()
command = conexion.CreateCommand()
...
command.Transaction = transaccion
command.ExecuteNonQuery()
transaccion.Commit()
```
Se puede cancelar con `transaccion.Rollback()`

# DataSets #
## ¿Qué es un DataSet? ##
_El DataSet de ADO.NET es una representación de datos residente en memoria que proporciona un modelo de programación relacional coherente independientemente del origen de datos que contiene._ http://msdn.microsoft.com/es-es/library/ss7fbaez%28VS.80%29.aspx

## Ejemplo ##
Ver ejemplo en AdoOracle.

El proposito de un DataAdapter es conectar la capa del Data Provider con un DataSet

Los DataReaders son limitados: sólo lectura y sólo adelante. Los DataSets no son dependientes de la Base de Datos.

Recursos avanzados: `DataSet.Update`, `DataRelations`

# Ejemplos #
  * AdoOracle
  * AdoMySql