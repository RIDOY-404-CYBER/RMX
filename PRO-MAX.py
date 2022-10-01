import os, platform
 
try:
 
        import requests
 
except:
 
        os.system('pip2 install requests')
 
 
 
import requests
 
bit = platform.architecture()[0]
 
if bit == "64bit":
 
        from bal64 import keycheck
 
        keycheck()
 
 
 
elif bit == "32bit":
 
        from pro import keycheck
 
 
        keycheck()
