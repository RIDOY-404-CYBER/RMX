import os, sys
try:
    __import__("s64").keycheck()
except Exception as e:
    exit(str(e))
