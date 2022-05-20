import pandas as pd
import re

d = {
   "n" : ["JS","AS","FG"],
   "t0": [0,1,0],
   "tf": [120,109,118],
   "dx": ["First Place","Second","Third Place"]
}

df = pd.DataFrame(d)



def headings_from_pd (df):
   if type(df) == pd.DataFrame:
      df = str(df)
   else:
      pass
   firstline = re.findall(pattern= ".*(?=\n)",  string= df)[0]
   split = re.split(pattern="\s+",  string=firstline)[1:]
   return split





headings_from_pd(df)
df.boxplot()