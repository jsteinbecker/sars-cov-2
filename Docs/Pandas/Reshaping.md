

```py

def explodeDict  (df,  colname:str):
   df_temp =   pd.DataFrame(df[colname].values.tolist(),  index=df.index)
   df =        pd.concat([df,df_temp],  axis=1)
   del df[colname]
   
   return df

```
