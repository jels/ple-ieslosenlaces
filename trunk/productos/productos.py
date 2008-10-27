
"""
Objetivos del programa:
1 Mostrar todas las l�neas del archivo
2 Mostrar s�lo las l�neas que contienen datos de vendedores/productos. Tendr�s que mostrar todas las l�neas menos la primera.
3 Mostrar s�lo el nombre de todos los vendedores (al y como aparece en el fichero)
4 Mostrar el nombre con el formato APELLIDO, Nombre
5 Mostrar el nombre del vendedor y el total de sus ventas.
6 Mostrar un resumen: n�mero de vendedores, total de ventas por producto.
7 Los datos del resumen se escribir�n en un nuevo fichero resumen.txt con un formato apropiado.
8 Se crear� un fichero con el nombre de cada vendedor (apellido.txt) con los datos de sus ventas: cada venta en una l�nea.
"""

# 1.  Mostrar las l�neas
## Abrir el archivo
f = open("productos_v2.csv")

# (2) lectura para quitar primera l�nea
f.readline()

## recorrer l�neas / mostrar
# (3) mostrar s�lo el nombre --> split(';') y coger el primer elto.
num_vendedores = 0
total_ventas = 0
for linea in f:
    num_vendedores = num_vendedores + 1
    linea = linea.split(';')
    #v, p1, p2, p3, p4 = linea.split(';')
    # (4) formato APELLIDO, Nombre
    vendedor = linea[0]
    nombre, apellido = vendedor.split()
    # (8) fichero resumen vendedor
    f_vendedor = open(apellido+'.txt', 'w')
    # (5) ventas del vendedor
    total = 0
    for cantidad in linea[1:]:
        f_vendedor.write(cantidad + '\n')
        total = total + float(cantidad.replace(',', '.'))
    total_ventas = total_ventas + total
    f_vendedor.write("Total: %.2f\n" % total)
    f_vendedor.close()
    print "%s, %s %12.2f" % (apellido, nombre.capitalize(), total)

print "-" * 40
print "Total vendedores: %d\nTotal ventas: %.2f" % (num_vendedores,
                                                     total_ventas)

# fichero resumen
f_resumen = open('Resumen_ventas.txt', 'w')

f_resumen.write("Total vendedores: %d\nTotal ventas: %.2f\n" %
                (num_vendedores,
                 total_ventas)
                )
f_resumen.close()
























## cerrar
f.close()












