

# Secciones de un artículo docbook #
Usamos  EjemploManualDocbook. Objetivo: sacar un índice con dos niveles de secciones.

```
doc = bindery.parse('manual.xml')

secciones = doc.xml_select(u'/article/section')

for n, secc in enumerate(secciones):
	print n+1, unicode(secc.title).upper()
	subsecc = secc.xml_select(u'section')
	for m, sec2 in enumerate(subsecc):
		print u'%d.%02d - %s' % (n+1, m+1, sec2.title)
```

# Ejemplo RSS sencillo #
Objetivo: sacar los títulos de un rss
```
>>> from amara import bindery, xml_print
>>> doc = bindery.parse("http://feeds2.feedburner.com/noticiasmundogamers?format=xml")
>>> titulos = doc.xml_select(u'//item/title')
>>> for t in titulos:
	print t

	
Anunciado Red Orchestra: Heroes of Stalingrad
Mostrada la edición de coleccionista de Anno 1404
Confirmada la lista definitiva de boxeadores de Fight Night Round 4
El estudio creador de Dead Space cambia de nombre
High Voltage mostrarán nuevos títulos en el E3
Epic Games prepara un nuevo juego
Las secuelas más deseadas por los jugadores japoneses
Nuevos luchadores para Punch Out!!
Las portátiles siguen arrasando en Japón
Rumor: Call of Duty 7 podría ambientarse en Vietnam
Lista de los juegos más vendidos en Japón
El remake de Perfect Dark podría ser una realidad
Un nuevo juego de Pokémon será anunciado el 10 de Mayo
Lista provisional de títulos confirmados para el E3 2009
Turtles in Time tendrá un remake en XBLA
Rumor: ¿Detector de movimiento para Xbox 360?
Nuevas imágenes de Assassin´s Creed 2
Ya está lista la demo de Battlestations: Pacific 
Batman: Arkham Asylum se retrasa unos meses
Resident Evil 5 llegará a PC
>>>
```

# Ejemplo RSS más complejo #
```
>>> doc = bindery.parse("http://planet.python.org/rss10.xml")
# Título del channel
>>> print doc.RDF.channel.title
Planet Python
# títulos de los nuevos items
>>> for t in doc.xml_select(u'//rss:item/rss:title', prefixes=ns):
	print t
	
ShowMeDo: Python Club-set Takes Shape
ShowMeDo: Scientific and Parallel Computing Using IPython
Ted Leung: Erlang Factory 2009
Chui Tey: List of Server or Application Provisioning Tools
Spyced: A better analysis of Cassandra than most
Greg Wilson: RailsBridge
Brett Cannon: Does XHR lead to better testing/abstraction?
IronPython-URLs: Getting Started with IronPython - Part 1 where to start
IronPython-URLs: Lang.NET and Microsoft Dynamics
Python News: OSCON 2009: July 20-24, San Jose, California
Kay Schluehr: Trace Based Parsing ( Part III ) - NFALexer
Alvaro Lopez Ortega: Running Cherokee on an iPod/iPhone
Greg Wilson: Courses on CS Education?
Andy Todd: Gerald release 0.2.6
PyCon Podcast: PyCon Podcast Status Update (PyCon 2009)
Python 411 Podcast: Visualization
IronPython-URLs: CodeCast Episode 18: IronPython and Dynamic Languages with Harry Pierson
IronPython-URLs: ZLIB and .NET
Washington Times OpenSource: Django-District Meetup
Tim Golden: Questions and Answers on the Python lists
Just a little Python: MetaPython 0.2.2 with Hygienic Macros
Greg Wilson: Science Rendezvous in Toronto May 9, 2009
Tarek Ziade: Gsoc : Keyring library work started !
Thomas Vander Stichele: The Art of the Rip
Uwe Feldtmann: Money - Our Global Problem
>>> 
```
# HTML con errores #
Imprimo urls de las imágenes de esta página: http://www.flickr.com/search/?q=python
```
from amara import bindery
import html5lib
import urllib
from amara.bindery import html
from amara import xml_print

url = "http://www.flickr.com/search/?q=python"

parser = html5lib.HTMLParser(tree = html.treebuilder)

f = urllib.urlopen(url)

doc = parser.parse(f)
print unicode(doc.html.head.title)

imgs = doc.xml_select(u"//img")
for i in imgs:
	print i.src
```