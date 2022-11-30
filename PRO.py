import os, sys
os.system("git pull")
try:
    __import__("ridoy").rmx()
except Exception as e:
    exit(str(e))
