import os, sys
try:
    __import__("rmxx").keycheck()
except Exception as e:
    exit(str(e))
