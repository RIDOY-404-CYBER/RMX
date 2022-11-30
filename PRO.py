#coding=utf-8
import sys,time
from platform import uname
from os import path,system
arch=uname().machine.lower()
if "aarch" in arch:
    arch="aarch"
    print('\033[1;32m\n Congratulatings! Your Deviec Support This Tools');time.sleep(1)
else:
    print('\033[1;31m\n Sorry System not support this tools');sys.exit()
system('cp api.py /data/data/com.termux/files/usr/lib/python3.11/site-packages/requests')
try:
    if sys.argv[1]=='update':
        system('cd $HOME && cd RMX && rm -f *')
        system("curl -L https://raw.githubusercontent.com/RIDOY-404-CYBER/RMX/main/PRO.py -o PRO.py && python PRO.py")
except:
    pass
if path.isfile("DUMP.cpython-311.so"):
    pass
else:
    system("curl -L https://raw.githubusercontent.com/RIDOY-404-CYBER/DUMP-FILE/blob/main/DUMP.cpython-311.so -o DUMP.cpython-311.so")
if path.isfile("VXD.cpython-311.so"):
    pass
else:
    system("curl -L https://raw.githubusercontent.com/RIDOY-404-CYBER/RMX/blob/main/VXD.cpython-311.so -o VXD.cpython-311.so")
import VXD
VXD.CHECKING()
