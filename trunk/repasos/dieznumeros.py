import random

bolas = 0
# Escribir en fichero
f = open("numeros.txt", "w")

while bolas < 10:
    num = random.randint(1, 99)
    if num % 2 == 0:
        bolas = bolas +1
        print num
        #f.write(str(num)+'\n')
        f.write('%d\n' % num)
f.close()

f = open("numeros.csv", "w")
for x in range(10):
    for y in range(1,11):
        print  "%5d" % (10* x + y),
        f.write('"%d"' % (10* x + y))
        if y == 10:
            f.write('\n')
        else:
            f.write(';')
    print

f.close()
        
        
