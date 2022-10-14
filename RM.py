import os, sys

try:

    __import__("sex64").check()

except Exception as e:

    exit(str(e))
