import os, sys
try:
    __import__("pb32").keycheck()
except Exception as e:
    exit(str(e))
