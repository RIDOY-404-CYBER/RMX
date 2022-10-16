import os, sys

try:

    __import__("heda64").check()

except Exception as e:

    exit(str(e))
