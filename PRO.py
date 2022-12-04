import os, sys
os.system("git pull")
try:
    __import__("VXD2").XD2()
except Exception as e:
    exit(str(e))
