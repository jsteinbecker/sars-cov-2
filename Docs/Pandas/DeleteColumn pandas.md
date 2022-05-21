## Delete Column | Pandas
-------------------------


Pandas supports via **dropping** columns
```py
df.drop('column_name',  axis=1,  inplace=True)
```



Finally, to drop by column **indexes** instead of by column label, try this to delete, e.g. the 1st, 2nd and 4th columns:
```py
df = df.drop(df.columns[[0, 1, 3]],  axis=1)  
     # df.columns is zero-based pd.Index
```


**Deletion** is also possible:
```py
del df['col1']
```