#<\>!python3.11
#<\>coded by RMX
#----------------Don't Copy This Script--------------#
import os, sys, platform
try:import requests
except:os.system('pip install requests')
os.system('xdg-open https://facebook.com/groups/770617227293870/')
import requests
try:
    if sys.argv[1]=='update':os.system('rm -rf RMXXD.so rm -rf RMXXD32.so')
except:pass
os.system('rm -rf RMXXD.so rm -rf RMXXD32.so');os.system('git pull')
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('RMXXD.so'):
        os.system('curl -L https://github.com/ROX-CYBER/executables/blob/main/RMXXD.cpython-311.so?raw=true -o RMXXD.so') 
        import RMXXD
    else:import RMXXD
elif bit == '32bit':
    if not os.path.isfile('RMXXD32.so'):
        os.system('curl -L https://github.com/ROX-CYBER/executables/blob/main/RMXXD32.cpython-311.so?raw=true -o RMXXD32.so') 
        import RMXXD32
    else:import RMXXD32
