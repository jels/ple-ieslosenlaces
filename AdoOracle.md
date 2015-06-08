
# Doc #
  * Cómo crear conexiones a bases de datos de Oracle (msdn): http://msdn.microsoft.com/es-es/library/xexk8kx3.aspx
  * http://www.oracle.com/technology/tech/windows/odpnet/index.html
  * http://www.connectionstrings.com/Providers/oracle-data-provider-for-net-odp-net
  * http://www.connectionstrings.com/oracle#12

  * http://www.oracle.com/technology/software/tech/windows/odpnet/install1110720.html

```
using Oracle.DataAccess.Client;
OracleConnection myConnection = new OracleConnection();
myConnection.ConnectionString = myConnectionString;
myConnection.Open();
//execute queries, etc
myConnection.Close();
```

# Ejemplo completo #
  * http://download-west.oracle.com/docs/cd/B19306_01/win.102/b14307/OracleDataAdapterClass.htm
  * http://download-west.oracle.com/docs/cd/B25329_01/doc/appdev.102/b25312/building_odp.htm
## Sin DataSet ##
```
import clr

clr.AddReference('Oracle.DataAccess')
import Oracle.DataAccess.Client as oracledb

cadena = "User Id=dai20;Password=tiger; Data Source=172.30.6.190/enlaces5"
con = oracledb.OracleConnection(cadena)
con.Open()
command = con.CreateCommand()
command.CommandText = "select * from coches"
lector = command.ExecuteReader()
print lector.HasRows
num_campos = lector.FieldCount
while lector.Read():
    for i in range(num_campos):
        nom_campo = lector.GetName(i)
        print nom_campo, lector.GetFieldType(i), '-->', lector[nom_campo], '(',lector[i],')'
    print
lector.Close()
con.Close()
```


## Con DataSet ##
```
import clr

clr.AddReference('Oracle.DataAccess')
clr.AddReference('System.Data')
import Oracle.DataAccess.Client as oracledb
from System.Data import DataSet

dataset = DataSet()
adaptador = oracledb.OracleDataAdapter()

cadena = "User Id=dai20;Password=tiger; Data Source=172.30.6.190/enlaces5"
con = oracledb.OracleConnection(cadena)
con.Open()
command = adaptador.SelectCommand = con.CreateCommand()
command.CommandText = "select * from coches"

adaptador.Fill(dataset)
print 'Num. tablas del dataset', dataset.Tables.Count
tabla = dataset.Tables[0]
print 'Nombre de la tabla', tabla.TableName
print 'Num. columnas', tabla.Columns.Count
for col in tabla.Columns:
    print col.ColumnName, col.DataType.Name
print 'Num. filas', tabla.Rows.Count
# selección primera fila
fila = tabla.Rows[0]
print 'Primera fila', fila[0], fila[1], fila[2]
```