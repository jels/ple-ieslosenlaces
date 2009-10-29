"""
0. Crear los dos ficheros externos
1. Abrir desde el programa y mostrar en pantalla

"""

# Abrir ficheros --> f = open(ruta)
fcarta = open("carta.txt")
fclientes = open('clientes.txt')
# leer fichero --> contenido = f.read()
carta = fcarta.read()
#clientes = fclientes.read()
for cliente in fclientes:
    nombre, apellido, deuda = cliente.split()
    nombre_completo = nombre + ' ' + apellido.upper()
    carta_tmp =  carta.replace('$CLIENTE$', nombre_completo)
    carta_tmp = carta_tmp.replace('$DEBE$', deuda)
    print carta_tmp
    f = open(nombre+'_'+apellido+'.txt', 'w')
    f.write(carta_tmp)
    f.close()
    
    raw_input()
# mostrar contenido --> print contenido
##print carta
##print '* ' * 20
##print clientes
