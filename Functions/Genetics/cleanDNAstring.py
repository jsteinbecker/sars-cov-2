import re

def cleanDNA (seq:str):
   seq = re.sub("\d","",seq)
   seq = re.sub("\s","",seq)
   seq = re.sub("\n","",seq)

   return seq
