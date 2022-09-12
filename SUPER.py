import os, sys
try:
    __import__("mx64").keycheck()
except Exception as e:
    exit(str(e))