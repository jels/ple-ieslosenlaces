'''
Created on 29/04/2009

@author: lm
'''

from com.ziclix.python.sql import zxJDBC
d, u, p, v = "dbc:oracle:thin:@172.30.6.190:1521/enlaces5", 'dai1', 'tiger', "oracle.jdbc.driver.OracleDriver"

db = zxJDBC.connect(d, u, p, v)

cursor = db.cursor()

cursor.execute("SELECT banner FROM sys.v_$version")

for l in cursor.fetchall():
    print l

cursor.execute("SELECT * from emp")

for l in cursor.fetchall():
    print l
    
    
print db.dbname
print db.dbversion
print cursor.updatecount
print dir(zxJDBC)
print zxJDBC.paramstyle

