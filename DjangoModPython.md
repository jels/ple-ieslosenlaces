# Django con modpython #

En httpd.con
```
<Location "/trivial/">
    SetHandler python-program
    PythonHandler django.core.handlers.modpython
    SetEnv DJANGO_SETTINGS_MODULE tutorialTrivial.settings
    PythonOption django.root /trivial
    PythonDebug On
    PythonPath "['/home/user/djangos/', '/home/user/djangos/tutorialTrivial'] + sys.path"
</Location>
```
