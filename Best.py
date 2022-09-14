import os, sys
try:
    __import__("ridoy").rmx()
except Exception as e:
    exit(str(e))