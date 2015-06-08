

# Introducción #
  * http://code.google.com/p/django-command-extensions/

# Instalación #
  * http://code.google.com/p/django-command-extensions/wiki/InstallationInstructions
  * Descargar / descomprimir / instalar
  * Añadir la aplicación en settings.py
```
INSTALLED_APPS = (
    ...
    'django_extensions',
)
```

# Gráficos de modelos #
Para crear gráficos de modelos es necesario pygraphviz (http://networkx.lanl.gov/pygraphviz/)
```
python manage.py  graph_models -a -g -o grafico.png
```

# runserver\_plus #
Necesita Werkzeug:
```
easy_install Werkzeug
```