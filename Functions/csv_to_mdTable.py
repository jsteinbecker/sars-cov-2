import re

"""
SAMPLE DATA
############
"""
line = "Prokofiev,Russia Under the Mongolian Yolk (Nevsky),BC,15 min,4,5"
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
####################
MAKE TABLE FUNCTION
####################
"""
def maketable  (head,body): 
   print(f'\n{ formatter(head) }\n{ makediv(head) }\n{ formatter(body) }\n')

maketable(header,line)
formatter("Mahler,Symphony No 2: Resurrection- I. Totenfeier,BC,$30m$,4,4")