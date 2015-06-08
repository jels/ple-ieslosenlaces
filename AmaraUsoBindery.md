

http://wiki.xml3k.org/Amara2/QuickRef#Amarabindery

Basado en el ejemplo EjemploLibrosXml

# Leer documento #
```
from amara import bindery
doc = bindery.parse('libros.xml')
```

# Mostrar documento #
```
from amara import xml_print
xml_print(doc)
```

# Búsqueda sencilla con XPath #
## sin namespaces ##
```
>>> libros = doc.xml_select(u'//libro')
>>> len(libros)
5
```

## con namespaces ##
```
>>> ns = {u'lib': u"http://www.ies-losenlaces.com/biblioteca"}
>>> doc.xml_select(u'//lib:libro', prefixes=ns)
```

# Recorrer elementos #
Imprime títulos de los libros:
```
>>> for libro in doc.biblioteca.xml_elements:
	print libro.titulo
```
Más pythonico:
```
>>> for l in iter(doc.biblioteca.libro):
	print l.titulo
```
Imprime títulos de los libros en español:
```
>>> for l in iter(doc.biblioteca.libro):
	if l.idioma == u'es':
		print l.titulo
```
Primer libro de la biblioteca:
```
>>> print doc.biblioteca.libro.titulo
Introducción a Python
```
Segundo libro de la biblioteca
```
>>> print doc.biblioteca.libro[1].titulo
Learning Python
```
# Manipulación #
Cambiamos el título al primer libro:
```
>>> doc.biblioteca.libro.titulo = u"Nuevo título"
>>> xml_print(doc.biblioteca.libro)
<libro xmlns="http://www.ies-losenlaces.com/biblioteca" idioma="es" lenguaje="python">
    <titulo>Nuevo título</titulo>
    <autor>
      <nombre>Benjamin</nombre>
      <apellido>Martínez</apellido>
    </autor>
  </libro>
```
Eliminamos el primer libro:
```
>>> del doc.biblioteca.libro
```

EjemplosUsoAmara

EjerciciosBindery