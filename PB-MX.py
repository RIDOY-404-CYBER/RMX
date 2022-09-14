import os, platform

try:

        import requests

except:

        os.system('pip2 install requests')



import requests

bit = platform.architecture()[0]

if bit == "64bit":

        from pbx64 import login

        rmx() 



elif bit == "32bit":

        from pbx32 import login 


        rmx()