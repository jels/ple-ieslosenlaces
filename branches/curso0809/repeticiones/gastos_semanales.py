"""
Control gastos semanales
"""

# procesar fichero
f = open("gastos.txt")

# INICIALIZAR VARIABLES
total = 0  # gasto total: todas las semanas
num_semanas = 0
semana_mas_num = 0
max_semana = 0

# bucle general del fichero
for linea in f:
    parcial_semana = 0
    num_semanas = num_semanas + 1
    for gasto in linea.split(): # recorre los distintos gastos de la semana
        # sumar los gastos en parcial_semana --> convertir a int antes
        parcial_semana = parcial_semana + int(gasto)
    total = total + parcial_semana
    if parcial_semana > max_semana:
        max_semana = parcial_semana
        semana_mas_num = num_semanas
    if num_semanas == 1 or parcial_semana < min_semana:
        semana_min_num = num_semanas
        min_semana = parcial_semana
            
        
print 'Total de gastos %10d' %  total
print 'Media semanal   %13.2f' % (total / float(num_semanas))
print 'Máximo semanal  %10d   (semana %d)' % (max_semana, semana_mas_num)
print 'Mínimo semanal  %10d   (semana %d)' % (min_semana, semana_min_num)
    
        
    

