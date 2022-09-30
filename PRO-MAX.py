import os, sys

try:

    __import__("pb64").keycheck()

except Exception as e:

    exit(str(e))
