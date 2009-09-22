"""
Ejercicios con el ejemplo curso
"""

curso = {'Pedro':
         {'nombre': 'Pedro de Pedro',
          'notas': {'Programacion': [8, 4, 5],
                    'Analisis': [4, 6, 7]}},
         'Ana':
         {'nombre': 'Ana Martínez',
          'notas': {'Programacion': [3, 4, 5],
                    'Sistemas': [4,6,8,9,9]}
          },
         'María':
         {'nombre': 'María Villa',
          'notas': {'Analisis': [6, 8],
                    'Programacion': [7,8,9],
                    'Sistemas': [8,8,9]
                    }
          }
         }

def lista_alumnos(curso):
    """ Imprime lista ordenada de alumnos"""
    #1. crear lista de alumnos
    lista = []
    for k in curso:
        lista.append(curso[k]['nombre'])
    #2. ordenar lista
    lista.sort()
    #3. imprimir
    for n, alumno in enumerate(lista):
        print "%2d. %s" % (n+1, alumno)

def lista_alumnos_asig(curso):
    aux = {}
    #1. crear aux
    for k in curso:
        for asig in curso[k]['notas']:
            if asig in aux.keys():
                aux[asig].append(curso[k]['nombre'])
            else:
                aux[asig] = [curso[k]['nombre']]
    #2. mostrar resultado
    for k in aux:
        print k.upper(), '*' * 20
        for n, alumno in enumerate(aux[k]):
            print "%2d. %s" % (n+1, alumno)

        
            
        
def aprueba_todo(notas):
    """Recibe diccionario de notas ..."""
    for asig in notas.keys():
        if sum(notas[asig])/len(notas[asig]) < 5:
            return False
    return True

def lista_aprobados(curso):
    """Muestra los que aprueban todo"""
    for al in curso.keys():
        if aprueba_todo(curso[al]['notas']):
            print curso[al]['nombre']
            

print '*' * 40
lista_alumnos(curso)
print '*' * 40
lista_alumnos_asig(curso)
print '*' * 40
lista_aprobados(curso)

