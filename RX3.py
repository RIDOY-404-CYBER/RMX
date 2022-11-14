import os, sys
try:
    __import__("RG6").check()
except Exception as e:
    exit(str(e))
