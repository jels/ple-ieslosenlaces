
#pide palabra en minúsculas

nombre = raw_input("Introduzca nombre (minúsculas): ")

#while nombre != nombre.lower():
while  nombre.islower() != True:
    nombre = raw_input("Introduzca nombre (minúsculas): ")

print 'nombre en minúsculas', nombre

                   
