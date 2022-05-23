import re

"""
SAMPLE DATA
############
"""
class sample :
   line =   "Prokofiev,Russia Under the Mongolian Yolk (Nevsky),BC,15 min,4,5"
   header = "Composer,Work,Ins.,Time,Vibe,Quality"


"""
LAMBDA FXS
###########
"""
# SUBSTITUTE , with |
formatter = lambda x: re.sub(","," | ",x)
# COUNT NEEDED COLUMN NUMBER
headercount = lambda x: x.count(",")
# MAKE MARKDOWN TABLE DIVIDER
makediv = lambda head: ((headercount(head)) * "---|" ) + "---"



"""

"""
def maketable  (head,body): 
   """
   -----------
   MAKE TABLE FUNCTION
   -----------
   """
   print(f'\n{ formatter(sample.head) }\n{ makediv(sample:head) }\n{ formatter(body) }\n')

"""
####################
GET MINUTES PRACTICED
####################
"""
def getMinutes (inp):
   mins = str(re.findall("\d*m",inp))
   minint = int(("".join(re.findall("\d+",mins))))
   return minint





















   
getMinutes("ghgj 78 h78 60m 68")

maketable(header,line)
formatter("Mahler,Symphony No 2: Resurrection- I. Totenfeier,BC,$30m$,4,4")