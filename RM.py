import os, sys

try:

    __import__("RG64").check()

except Exception as e:

    exit(str(e))
