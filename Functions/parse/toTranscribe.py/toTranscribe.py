#%%
import yaml
from yaml import load, dump, Loader, Dumper
import pandas as pd


# %%
data = """
Rogue One:
    composer : GIACCHINO
    movements : 
        - Good Luck Little Sister *CT
        - Your Father Would Be Proud *CO

HTTYD- The Hidden World :
    composer : POWELL
    movements : 
        - With Love Comes a Great Waterfall *VN
"""


y = yaml.load(data ,Loader=Loader)
y
# %% MOVE DATA TO DATAFRAME
df = pd.DataFrame(y)
df = df.T
df

# %% EACH MOVEMENT PROMOTED TO ROW
df = df.explode('movements')
df

# %% SEPARATE COMPOSERS LIST
list_of_composers = list(df.composer.unique())
list_of_composers

# %%
import re

# %% CHANGE COLUMN DTYPE
df['movements'] = df['movements'].astype("str")

# %% EXTRACT INSTRUMENT SIG
df['inst'] = df['movements'].str.extract("(\*\w\w)")
df['movements'] = df['movements'].str.replace("(\*\w\w)","",regex=True)

# %%
df

# %% CREATE PIVOT TABLE
df.pivot(columns="composer",index="movements")
# %%
