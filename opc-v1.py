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

opc = OpenOPC.open_client(host)
status_co = opc.connect(server)
#conn = psycopg2.connect(database)
#cur = conn.cursor()
#while status_co == True:


for i in range(len(var)):
	valor, quality, fecha = opc.read(var[i][1])
	fecha =time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(calendar.timegm(time.strptime(fecha,"%m/%d/%y %H:%M:%S"))))
	print fecha	
opc.close()

