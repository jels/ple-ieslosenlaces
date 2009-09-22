'''
Created on 29/04/2009

@author: lm
http://mail.python.org/pipermail/python-list/2002-August/158529.html
'''

from com.ziclix.python.sql import zxJDBC
from com.ziclix.python.sql.handler import OracleDataHandler

db = zxJDBC.connect(
    "jdbc:oracle:thin:@172.30.6.190:1521:enlaces5",
    "dai1",
    "tiger",
    "oracle.jdbc.driver.OracleDriver"
)
c = db.cursor()

# it's very important to use the appropriate datahandler so the
# proper casing of names is handle correctly
c.datahandler = OracleDataHandler(c.datahandler)

try:
    c.execute("create table sptest (x varchar2(20))")
except:
    pass

sp = "create or replace procedure procin (y in varchar2) is"
sp += " begin insert into sptest values (y); end;"
c.execute(sp)

sp = "create or replace procedure procinout (y out varchar2,"
sp += " z in varchar2) is begin insert into sptest values (z)"
sp += "; y := 'tested'; end;"
c.execute(sp)

c.execute("delete from sptest")
db.commit()

params = ['testProcIn']
c.callproc("procin", params)

params = [None, "testing"]
c.callproc("procinout", params)
assert params[0] == "tested"

print "*" * 10
c.execute("select * from sptest")
for a in c: print a

db.commit()
c.close()
db.close()
