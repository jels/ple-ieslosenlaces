

# Intro a django admin site #

  * http://docs.djangoproject.com/en/dev/ref/contrib/admin/

# Activar Django admin site #
  1. Añadir `django.contrib.app` a `INSTALLED_APPS`
  1. Determinar qué modelos se van a editar con el **admin**
  1. Para cada modelo se puede crear un `ModelAdmin`
  1. Instanciar un `AdminSite` y relacionar los modelos y ModelAdmin clases
  1. Introducir el AdminSite en el URLconf.


# Objetos ModelAdmin #

## Opciones ##

# Adaptando el admin #
  * http://lincolnloop.com/assets/Customizing_the_Django_Admin-EuroDjangoCon09.pdf
  * http://www.ibm.com/developerworks/opensource/library/os-django-admin/index.html
## ModelAdmin media ##
```
class ArticleAdmin(admin.ModelAdmin):
    class Media:
        css = {
            "all": ("my_styles.css",)
        }
        js = ("my_code.js",)
```
## Modificación de las plantillas de Admin ##
Los archivos de los templates están en el directorio de django `contrib/admin/templates/admin`
  * Crear un directorio admin en el directorio templates del proyecto.
  * Crear subdirectorios con el nombre de la aplicaciones (en minúsculas).

Plantillas clave:
  * admin/base.html
  * admin/index.html
  * admin/change\_form.html
  * admin/change\_list.html

Se pueden cambiar para:
  * Todo el proyecto: admin/change\_form.html
  * Una aplicación: admin/

<my\_app>

/change\_form.html
  * Un modelo: admin/

<my\_app>

/

<my\_model>

/change\_form.html

Se utiliza  {{ block.super }} para extender bloques.