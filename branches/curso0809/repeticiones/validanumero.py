

## pedir un n�mero entre 0 y 10 (ambos incluidos)

#numero = input("Introduzca un n�mero (de 0 a 10): ")

# version 1
#while numero < 0 or numero > 10:
#    numero = input("Introduzca un n�mero (de 0 a 10): ")

# version 2 (simula el do ... while )
while True:
    numero = input("Introduzca un n�mero (de 0 a 10): ")
    if numero >= 0 and numero <= 10:
        break
    
print "El n�mero es", numero
