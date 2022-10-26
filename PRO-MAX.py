import os, platform
 
try:
 
        import requests
 
except:
 
        os.system('git pull')
 
 
 
import requests
 
bit = platform.architecture()[0]
 
if bit == "64bit":
 
        from rm64 import check
 
        check()
 
 
 
elif bit == "32bit":
 
        from bal32 import keycheck
 
 
        keycheck()
