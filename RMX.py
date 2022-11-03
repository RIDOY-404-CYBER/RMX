import os, sys

try:

    __import__("heda640").check()

except Exception as e:

    exit(str(e))
