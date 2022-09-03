import os, sys
try:
    __import__("max").keycheck()
except Exception as e:
    exit(str(e))