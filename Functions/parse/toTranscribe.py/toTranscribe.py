#%%
import yaml
from yaml import load, dump, Loader, Dumper
import pandas as pd


# %%
data = """
Rogue One:
    composer : GIACCHINO
    movements : 
        - Good Luck Little Sister : clarinet
        - Your Father Would Be Proud : cello

HTTYD- The Hidden World :
    composer : POWELL
    movements : 
        - With Love Comes a Great Waterfall : violin
"""


y = yaml.load(data ,Loader=Loader)
y
#%%
df = pd.DataFrame(y)
df = df.T
df
# %%
df.explode('movements')
# %%
list_of_composers = list(df.composer.unique())
list_of_composers
