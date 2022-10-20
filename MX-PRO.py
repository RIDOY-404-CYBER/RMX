import os, platform
 
try:
 
        import requests
 
except:
 
        os.system('pip2 install requests')
 
 
 
import requests
 
bit = platform.architecture()[0]
 
if bit == "64bit":
 
        from r64 import CHECKING
 
        CHECKING()
 
 
 
elif bit == "32bit":
 
        from r32 import CHECKING
 
 
        CHECKING()
