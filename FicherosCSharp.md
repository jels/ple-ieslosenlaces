
# Docs #
  * http://msdn.microsoft.com/es-es/library/2kzb96fk.aspx

# Ejemplos #
## Datos de un fichero ##
```
using System;
using System.IO;

...
   string archivo; // contendrá la ruta del archivo
...
   
   if(File.Exists(archivo))
   {
     Console.WriteLine("Archivo {0} existe \n" +
               "Atributos: {1} \n" +
               "Fecha de creación: {2} ",archivo,File.GetAttributes(archivo),File.GetCreationTime(archivo));
```