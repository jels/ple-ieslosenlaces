'''
Created on 13/04/2010

@author: lm
'''

from java.lang import System, Integer
from java.util import Calendar, Date, GregorianCalendar



print Date()

c = GregorianCalendar()
dia = Integer.toString(c.get(Calendar.DATE))
mes = Integer.toString(c.get(Calendar.MONTH))
anyo = Integer.toString(c.get(Calendar.YEAR))

System.out.println(dia + '/' + mes + '/' + anyo)

