import os, sys
try:
    __import__("rm").keycheck()
except Exception as e:
    exit(str(e))