import os, sys
os.system("git pull")
try:
    __import__("VXD1").XD()
except Exception as e:
    exit(str(e))
