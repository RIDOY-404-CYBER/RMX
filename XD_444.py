import os, sys

try:

    __import__("GXXX").check()

except Exception as e:

    exit(str(e))
