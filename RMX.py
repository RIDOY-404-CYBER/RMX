import os, sys

try:

    __import__("up42").check()

except Exception as e:

    exit(str(e))
