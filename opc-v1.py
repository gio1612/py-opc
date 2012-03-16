import OpenOPC
import time
import calendar
import ConfigParser
from optparse import OptionParser
import psycopg2

cfg = ConfigParser.RawConfigParser()
cfg.read('srv.cfg')

host = cfg.get('SERVER_INFO', 'host')
server = cfg.get('SERVER_INFO', 'server')

var = cfg.items('VARIABLES')

#opc = OpenOPC.open_client('host')
#status_co = opc.connect('server')

db=cfg.get('DATA_BASE_INFO','dbname');
db_host=cfg.get('DATA_BASE_INFO','host');
db_user=cfg.get('DATA_BASE_INFO','user');
db_pass=cfg.get('DATA_BASE_INFO','password');

conn = psycopg2.connect('dbname='+db+' host='+db_host+' user='+db_user+' password='+db_pass)
cur = conn.cursor()

dato1 = ('100','good','03/15/12 01:00:00')
dato2 = ('10','bad','03/15/12 10:00:00')
dato = (dato1,dato2)

"""while status_co == True:
	for i in range(len(var)):
		dato = opc.read(var[i][0])
		n =time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(calendar.timegm(time.strptime(dato[i][2],"%m/%d/%y %H:%M:%S"))))
"""		
		if quality == 'Good':
			cur.execute("INSERT INTO variable_valor (variable,fecha,valor) VALUES ('%s', '%s', %f)", (var[i][0],fecha,valor))

cur.close()
conn.close()

#value, quality, t = opc.read('MULT_S_Prj_OS(1)::TON-HR-PEND')

#t = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(calendar.timegm(time.strptime(t,"%m/%d/%y %H:%M:%S"))))

#opc.close()

