
#pide palabra en min�sculas

nombre = raw_input("Introduzca nombre (min�sculas): ")

#while nombre != nombre.lower():
while  nombre.islower() != True:
    nombre = raw_input("Introduzca nombre (min�sculas): ")

print 'nombre en min�sculas', nombre

                   
