import re

"""
#############
CLEAN DNA STRING
Function
-------------
REMOVES DIGITS SPACES AND NEWLINE CHARACTERS FROM INPUT
#############
"""

def cleanDNA (seq:str):
   seq = re.sub("\d","",seq)
   seq = re.sub("\s","",seq)
   seq = re.sub("\n","",seq)

   return seq
