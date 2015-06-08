## Descargar el driver Oracle para Java: ##

  * http://download.oracle.com/otn/utilities_drivers/jdbc/111070/ojdbc6.jar

## Cargamos el driver en Eclipse: ##
- Seleccionamos el proyecto, y vamos a la pestaña Proyecto-Propiedades-Vía de construcción Java. En la pestaña Bibliotecas añadimos un .jar externo que es el driver "ojdbc6.jar".
```
Class.forName("oracle.jdbc.driver.OracleDriver");
```

## Creamos una conexión: ##
```
Connection conexion = DriverManager.getConnection("jdbc:oracle:thin:@ip_servidor_oracle:1521:cadena de conexión", "usuario", "password");
```

## Creamos el cursor: ##
```
Statement cursor = conexion.createStatement();
```

## Ejecutamos la sentencia y recogemos los resultados: ##
```
ResultSet resultados = cursor.executeQuery("select * from tabla");
ResultSetMetaData resul = resultados.getMetaData();
```

## Mostrar los resultados devueltos por la sentencia: ##
```
for(int r=1; r<=resul.getColumnCount(); r++)
        System.out.printf(resul.getColumnName(r)+" ");
	System.out.println();
	while(resultados.next()){
		for(int r=1; r <=resul.getColumnCount(); r++){
		    if (r == resul.getColumnCount())
			System.out.println(resultados.getString(r));
		    else
			System.out.printf(resultados.getString(r)+"-");			
		}
	}
```

## Cerramos la conexión con el servidor Oracle: ##
```
conexion.close();
```