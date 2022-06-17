# %% 
import random as rnd
import pandas as pd
import numpy as np

# %%
"DEFINING STATES NAMES"

def make_states (n:int):
    stateletters = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split(" ")
    states = ["State " + x for x in stateletters]
    return states[0:n]

 
states = make_states(26)
states



# %%
"RANDOMLY GEN STATES POPULATIONS"
rnd.seed(2)
pops = [rnd.randint(1, 20000) for x in range(len(states))]
pops

# %%
"CALC TOTAL POPULATION"
total_pop = sum(pops)
total_pop
# %%
data = {"total_pop" : total_pop , "population" : pops}
df = pd.DataFrame(data,index=states)
df
# %%
df['%pop'] = round (df["population"] / df["total_pop"]*100, 1)
df
# %%
"NATIONWIDE POP:REP RATIO"
total_reps = 275
people_per_rep =  total_pop / total_reps 
people_per_rep
# %%
"""REPS WITH FLOOR DIV"""
df["reps"] = total_reps * (df['%pop']/100) // 1
df
# %%
sum(df['reps'])
# %%
_pop = list(df['population'])
_rep = list(df['reps'])
# %%
"""GEOMETRIC MEAN OF DIVISOR DISCREPANCY OF DESERVED ELECTORS BY STATE"""
_y = []
for x in range(len(_pop)):
    y = _pop[x] / np.sqrt(_rep[x] * (_rep[x] +1))
    _y.append(round(y,3))
_y
# %%
df['divisor'] = _y
df.divisor
# %%
seats_to_fill = int(total_reps -  sum(df['reps']))
seats_to_fill
# %%
"""INDEX DF FROM 0 : # OF SEATS TO FILL"""
getsnewrep = df.sort_values("divisor")[0:seats_to_fill]
getsnewrep
print(list(getsnewrep.index))
# %%
df['addrep'] = getsnewrep['reps'] + 1
df
# %%
df['addrep'] = df['addrep'].fillna(df['reps'])
df
# %%
sum(df['addrep'])
# %%
