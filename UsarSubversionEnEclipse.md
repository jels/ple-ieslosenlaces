## Instalación de Subclipse ##



  * Abrimos eclipse y vamos a la pestaña 'Help' del menú
  * Pestaña 'Software Update' -> 'Search and Install...'
  * Seleccionamos la opción 'Search for new features to Install' y le damos a 'Next'
  * Pulsamos la opción de 'New Remote Remote Site'
  * En 'Name' escribimos Subclipse  y en 'URL' escribimos la dirección de donde descargaremos Subclipse: http://subclipse.tigris.org/update_1.0.x
  * Pulsamos 'OK' y se nos marcara para instalar Subclipse y pulsamos 'Next' hasta llegar al contrato de licencia, lo aceptamos le damos a 'Next' y 'Finish'
  * Nos saldra otra ventana, pulsamos en 'Install All' y nos pedirá reiniciar, le damos a 'Yes' y listo.

## Importar un proyecto del repositorio a Eclipse ##

  * File -> Import
  * Nos saldra una ventanita con distintas carpetas, abrimos el menu desplegable de la carpeta 'Other' y seleccionamos 'Checkout Projects from SVN' y le damos a 'Next'
  * Seleccionamos la opción 'Create a new repository location' y le damos a next, nos pedirá la direccion del repositorio, así que la escribimos, en nuestro caso: http://pepinon.inf.enlaces/plesvn
  * Nos saldrá el contenido de nuestro repositorio, elegimos la carpeta que queremos traer a nuestro pc y le damos a 'Next'
  * Seleccionamos la opción 'Check out as a project configured using the New Project Wizard' y debajo elejimos la revision que queramos o 'HEAD' si la que queremos es la última
  * Por ultimo elegimos el lenguaje Pydev y listo




Esta por terminar