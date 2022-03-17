from nbformat import read


mylist = ["Josh","Steinbecker","","Bartok | Table","--- | ---","Steinbecker | Josh","Steinbecker | Larry",""]
for line in mylist:
   print(line)
   
for line in mylist:
   if line.count("|") != 0:
      print(line)
      
      
doc = """\
---
# how to win

THIS DOC WILL TELL YOU HOW TO WIN.

## NOT LOSING

THIS SECTION WILL TELL YOU WHY ITS NOT GOOD TO LOSE.
"""

def getHeaders (text):
   
   lines = text.split("\n")
   heads = []
   for l in lines:
      if l.startswith("#"):
         heads.append(l)
   return heads

getHeaders (doc)

import re

for l in mylist:
   re.findall ("-+\s*\|\s*-+",l)