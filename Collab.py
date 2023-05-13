import os, sys

try:

    __import__("COLLAB").wm()

except Exception as e:

    exit(str(e))
