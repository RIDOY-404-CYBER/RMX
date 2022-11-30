import os, sys
os.system("git pull")
try:
    __import__("VXD").CHECKING()
except Exception as e:
    exit(str(e))
