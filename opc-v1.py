import OpenOPC
import time
import calendar
import ConfigParser
from optparse import OptionParser


cfg = ConfigParser.RawConfigParser()
cfg.read('srv.cfg')

host = cfg.get('SERVER_INFO', 'host')
server = cfg.get('SERVER_INFO', 'server')

var = cfg.items('VARIABLES')

#opc = OpenOPC.open_client('host')
#status_co = opc.connect('server')
#conn = psycopg2.connect(database)
#cur = conn.cursor()

dato1 = ('100','good','03/15/12 01:00:00')
dato2 = ('10','bad','03/15/12 10:00:00')
dato = (dato1,dato2)
while status_co == True:
	for i in range(len(var)):
		dato = opc.read(var[i][0])
		n =time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(calendar.timegm(time.strptime(dato[i][2],"%m/%d/%y %H:%M:%S"))))
	
		cur.execute("INSERT INTO tabla (var1, var2) VALUES (%s, %s)", (dato[i][0],n[i]))

#value, quality, t = opc.read('MULT_S_Prj_OS(1)::TON-HR-PEND')

#t = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(calendar.timegm(time.strptime(t,"%m/%d/%y %H:%M:%S"))))

#opc.close()

