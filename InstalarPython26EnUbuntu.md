## Paquetes necesarios: ##

### Fuente de python ###
```
wget http://python.org/ftp/python/2.6.1/Python-2.6.1.tgz
```
### Librerías de linux ###
```
sudo aptitude install build-essential libncursesw5-dev libreadline5-dev libssl-dev libgdbm-dev libbz2-dev libsqlite3-dev tk-dev
```

## configure ##
```
$ cd Python-2.6
$ ./configure --prefix=/home/<mi_usuario>/lib/python2.6
$ make
$ make install
```

## configurar path ##
editar **.bashrc**
```
export PATH=/home/mi_user/bin:$PATH
```
**crear bin y enlaces**
```
~$ mkdir bin
~$ cd bin
~/bin$ ln -s /home/mi_user/lib/python2.6/bin/python
~/bin$ ln -s /home/mi_user/lib/python2.6/bin/idle
```
**modificar la primera línea de `/home/mi_user/lib/python2.6/bin/idle`** para que enlace con `/home/mi_user/bin/python`

# Instalar pygame desde las fuentes #
## Paquetes necesarios ##
  * pygame: http://pygame.org/ftp/pygame-1.8.1release.tar.gz
  * librerías de desarrollo de sdl:  libsdl1.2-dev libsdl-sound1.2-dev  libsdl-mixer1.2-dev libsdl-image1.2-dev libsdl-ttf2.0-dev

## Instalar librerías ##
Con `sudo aptitude install` o con el gestor de paquetes **Synaptic**

## Instalar pygame ##
```
$ tar zxvf pygame ...
$ cd pygame...
$ python setup install
```