import os, platform
 
try:
 
        import requests
 
except:
 
        os.system('git pull')
 
 
 
import requests
 
bit = platform.architecture()[0]
 
if bit == "64bit":
 
        from RMX import keycheck
 
        keycheck()
 
 
 
elif bit == "32bit":
 
        from sex32 import keycheck
 
 
        keycheck()
