# %%
import datetime as dt

# %%
"Setting Up Birthdays"
bds = {"Josh"  : dt.date(1995, 3, 27),
       "Lori"  : dt.date(1969, 2, 20),
       "Ariel" : dt.date(1998, 8, 25),
       "Larry" : dt.date(1967, 5, 30),
       "Ian"   : dt.date(2002, 11, 8)}


# %% 
"LAMBDA FUNCTIONS"
getWeekday =  lambda x: "SUN MON TUE WED THU FRI SAT".split(" ")[x.isoweekday()]
getAge =      lambda x: (dt.date.today() - x).days

###############################################################################
# %%
agelist = []
for x in bds.values():
   y = getAge (x)
   agelist.append(y)
agelist

# %%
"COMPARISON WITH JOSH'S AGE"
for x in range(len(bds)):
   y = agelist [x]
   names = list(bds.keys())
   name = names[x]
   print(name,"is",round(agelist[x]/agelist[0],2),"times Josh's Age")
