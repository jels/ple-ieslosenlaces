edad = raw_input("introduzca la edad: ")
try:
    edad = int(edad)
    edad = edad + 1
    print "Nueva edad", edad
except ValueError:
    print "Valor incorrecto"

