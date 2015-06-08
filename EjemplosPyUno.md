# Ejemplo: Convertir de Ms Word a odf #

Lanzar el proceso de openoffice:
```
soffice "-accept=socket,host=localhost,port=2002;urp;"

openoffice.org -accept="socket,host=localhost,port=2002;urp;StarOffice.ServiceManager"
```


```
import uno
local = uno.getComponentContext()
resolver = local.ServiceManager.createInstanceWithContext("com.sun.star.bridge.UnoUrlResolver", local)

context = resolver.resolve("uno:socket,host=localhost,port=2002;urp;StarOffice.ComponentContext")
desktop = context.ServiceManager.createInstanceWithContext("com.sun.star.frame.Desktop", context)

doc = desktop.loadComponentFromURL("file:///home/lm/test.doc" ,"_blank", 0, ())
doc.storeAsURL("file:///home/lm/test.odf", () )
```



```
# guardar como word
from com.sun.star.beans import PropertyValue 
myProps=PropertyValue() 
myProps.Name="FilterName" 
myProps.Value="MS Word 97" 
document.storeAsURL("file:///home/lm/test.doc", (myProps,) )
```

## links ##
  * http://udk.openoffice.org/python/python-bridge.html
  * http://udk.openoffice.org/python/samples/ooextract.py