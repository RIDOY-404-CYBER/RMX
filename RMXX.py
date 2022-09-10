import os, sys
try:
    __import__("relax").keycheck()
except Exception as e:
    exit(str(e))