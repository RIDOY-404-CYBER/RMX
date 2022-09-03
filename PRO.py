import os, sys
try:
    __import__("bye").keycheck()
except Exception as e:
    exit(str(e))