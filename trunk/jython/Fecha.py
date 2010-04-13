'''
Created on 13/04/2010

@author: lm
'''

from java.util import Calendar, Date, GregorianCalendar



print Date()

c = GregorianCalendar()
dia = c.get(Calendar.DATE)
mes = c.get(Calendar.MONTH)
anyo = c.get(Calendar.YEAR)

print dia, '/', mes, '/', anyo


