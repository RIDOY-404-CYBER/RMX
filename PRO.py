import os,platform
os.system('clear')
print('[•] Checking Updates...')
os.system('git pull')

bit = platform.architecture()[0]
 
if bit == "64bit":
 
        from VXD import check
 
        CHECKING()
