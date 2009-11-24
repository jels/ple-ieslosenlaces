# -*- encoding: utf-8 -*-

'''
Created on 17/11/2009

@author: lm
'''

def crea_tabla(ruta):
    ''' crea_tabla(ruta) --> devuelve matriz
    
    devuelve matriz de datos a partir de un
    nombre de fichero pasado como ruta
    '''
    # abrir archivo
    try:
        f = open(ruta)
    except IOError:
        print 'El archivo no existe'
        return None
    # crear tabla vacía
    tabla = []
    # procesar archivo línea a línea
    primera = True
    for linea in f:
        if primera == True:
            primera = False
        else:
            # print linea,
            equipo = linea.strip()
            equipo = equipo.split(';')
            for i in range(1, len(equipo)):
                equipo[i] = int(equipo[i])
            tabla.append(equipo)
                
                
    ## primera l�nea no interesa
    
    ## split troceando por ';'
    
    ## conversiones oportunas de cadena a entero
    
    ## a�adir nueva lista a tabla vac�a 
    
    # cerrar archivo
    f.close()
    # devolver la nueva lista de listas creada
    
    return tabla


def puntos(equipo):
    '''
    puntos[lista_equipo] --> entero
    
    calcula los puntos que tiene un equipo.
    partidos ganados * 3 + partidos empatados
    '''
    return equipo[2]*3 + equipo[3]

def puntos_equipos(tabla):
    ''' imprime equipo y puntos
    '''
    for eq in tabla:
        print u"%-15s %3d" % (eq[0], puntos(eq))
        # u'cadena' --> unicode

# pprint(datos_liga)  # pprint para imprimir en bonito
def test():
    datos_liga = crea_tabla(r'datos\liga09.csv')
    equipo1 = datos_liga[0]
    print equipo1[0]
    print datos_liga[0][0]
    print datos_liga[0][0][0]




def valor_goles(eq1, eq2):
    '''valor_goles(eq1, eq2) --> devuelve -1 / 0 /1
    Resta a los goles a favor (pos 5) los goles
    en contra (pos 6)
    '''
    p_eq1 = eq1[5]- eq1[6]
    p_eq2 = eq2[5] - eq2[6]
    if p_eq1 < p_eq2:
        return 1
    elif p_eq1 == p_eq2:
        return 0
    else:
        return -1

def ordena_puntos(eq1, eq2):
    '''ordena_puntos(eq1, eq2) --> compara por puntos
    '''
    p_eq1 = puntos(eq1)
    p_eq2 = puntos(eq2)
    if p_eq1 < p_eq2:
        return 1
    elif p_eq1 == p_eq2:
        return valor_goles(eq1, eq2)
    else:
        return -1

def nombres(tabla):
    ''' nombres(tabla) --> devuelve lista de nombres
    '''
    res = []
    for li in tabla:
        res.append(li[0])
    return res

def seis_primeros(tabla):
    '''devuelve los seis primeros de la 
    clasificación con el formato: nombre, puntos
    '''
    tabla.sort(ordena_puntos)
    res = []
    for x in range(6):
        res.append([tabla[x][0], puntos(tabla[x])])  # nombre y puntos
    return res
