import OpenOPC
import time
import calendar
from optparse import OptionParser


opc = OpenOPC.open_client('192.168.2.100')

opc.connect('OPCServer.WinCC')
value, quality, t = opc.read('MULT_S_Prj_OS(1)::TON-HR-PEND')

t = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(calendar.timegm(time.strptime(t,"%m/%d/%y %H:%M:%S"))))

opc.close()

