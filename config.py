import ConfigParser

config = ConfigParser.RawConfigParser()

# When adding sections or items, add them in the reverse order of
# how you want them to be displayed in the actual file.
# In addition, please note that using RawConfigParser's and the raw
# mode of ConfigParser's respective set functions, you can assign
# non-string values to keys internally, but will receive an error
# when attempting to write to a file or when you get it in non-raw
# mode. SafeConfigParser does not allow such assignments to take place.
config.add_section('SERVER_INFO')
config.set('SERVER_INFO', 'host', '192.168.2.100')
config.set('SERVER_INFO', 'server', 'OPCServer.WinCC')
config.add_section('VARIABLES')
config.set('VARIABLES', 'TON-HR-PEND', 'MULT_S_Prj_OS(1)::TON-HR-PEND')
config.set('VARIABLES', 'TON-HR-BAL', 'MULT_S_Prj_OS(1)::TON-HR-BAL')
config.add_section('DATA_BASE_INFO')
config.set('DATA_BASE_INFO', 'host', '192.168.2.19')
config.set('DATA_BASE_INFO', 'dbname', 'SI')
config.set('DATA_BASE_INFO', 'user', 'eseprin')
config.set('DATA_BASE_INFO', 'password', 'eseprin')
# Writing our configuration file to 'example.cfg'
with open('srv.cfg', 'wb') as configfile:
    config.write(configfile)
