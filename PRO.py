import os, sys
try:
    __import__("rmx").keycheck()
except Exception as e:
    exit(str(e))