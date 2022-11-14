import os, sys
try:
    __import__("UPM2").check()
except Exception as e:
    exit(str(e))
