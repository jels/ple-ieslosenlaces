from math import sqrt

def es_primo(numero):
    for x in range(2,round(sqrt(numero)) +1 ):
        if numero % x == 0:
            return False
    return True

def pide():
    num = input("Introduzca un n�mero par: ")
    while num % 2 != 0:
        num = input("Introduzca un n�mero par: ")
    return num

def main():
    num = pide()
    for x in range(2, num/2 +1):
        if es_primo(x):
            y = num - x
            if es_primo(y):
                print x, '+', y, '=', num
                # break   --> mostrar s�lo uno
                

if __name__ == '__main__':
    main()
        
    
    
    
