"""
Calcular el menor de tres números
"""
x = 14
y = 10
z = 24
# forma 1
if x <= y and x <= z:
    menor = x
elif y <= x and y <= z:
    menor = y
else:
    menor = z

print 'El menor es (#1)', menor

# forma 2
if x <= y:
    if x <= z:
        menor = x
    else:
        menor = z
else:
    if y <= z:
        menor = y
    else:
        menor = z
print 'El menor es (#2)', menor

# forma 3
menor = x
if y < menor:
    menor = y
if z < menor:
    menor = z
    
print 'El menor es (#3)', menor


# forma 4
print 'El menor es (#4)', min(x, y, z)
