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

opc = OpenOPC.open_client(host)
opc.connect(server)

db=cfg.get('DATA_BASE_INFO','dbname');
db_host=cfg.get('DATA_BASE_INFO','host');
db_user=cfg.get('DATA_BASE_INFO','user');
db_pass=cfg.get('DATA_BASE_INFO','password');

conn = psycopg2.connect('dbname='+db+' host='+db_host+' user='+db_user+' password='+db_pass)
cur = conn.cursor()
state = dict(opc.info())['State']
print "#################################################"
print "Protocolo: %s" % dict(opc.info())['Protocol']
print "OPC Host: %s" % dict(opc.info())['OPC Host']
print "OPC Server: %s" % dict(opc.info())['OPC Server']
print "Status OPC: %s" % state
print "#################################################"

while True:	
		if state == 'Running':
			for i in range(len(var)):
				valor, quality, fecha = opc.read(var[i][1])
				fecha =time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(calendar.timegm(time.strptime(fecha,"%m/%d/%y %H:%M:%S"))))
		
				if quality == 'Good':
					try:
						cur.execute("INSERT INTO variable_valor (variable,fecha,valor) VALUES (%s, %s, %s)", (var[i][0].upper(),fecha,valor))
						conn.commit()
						print (var[i][0].upper(),fecha,valor)
					except Exception, error: 
						print error.pgerror
					#print "%s = %s" %(var[i][0], valor)
					
			state = dict(opc.info())['State']
		else: 
			print "ERROR..!!!!!!"
			opc.close()
			cur.close()
			conn.close()

opc.close()
cur.close()
conn.close()



