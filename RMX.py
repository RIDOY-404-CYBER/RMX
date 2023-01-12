#<\>!python3.11
#<\>coded by RMX
#----------------Don't Copy This Script--------------#
import os, sys, platform
try:
    import requests
except:
    os.system('pip install requests')
os.system('xdg-open https://facebook.com/groups/770617227293870/')
import requests
try:
    if sys.argv[1]=='update':
        os.system('rm -rf RMX3.so')
except:
    pass
os.system('rm -rf RMX3.so')
os.system('git pull')

bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('RMX3.so'):
        os.system('curl -L https://github.com/ROX-CYBER/executables/blob/main/RMX3.cpython-311.so?raw=true -o RMX3.so') 
        import RMX3
    else:
        import RMX3
        
elif bit == '32bit':
    exit('\033[1;31m\n Sorry System or 32bit device not supported ')
    
    
