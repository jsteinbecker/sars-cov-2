

# Filter DF:
```
filterdf = df [df ['col'] == value]
```

# New Column from Old:
`df['newcol'] = df['oldcol'] * Expressions`
> `df['partial year'] = df['year'] + (df['week']/ 52)`

# If-then Column:
`df.loc[df.AAA >= 5, "BBB"] = -1`
```
   AAA  BBB  CCC
0    4   10  100
1    5   -1   50
2    6   -1  -30
3    7   -1  -50
```

# Sort By
`df.sort_values(by=("Labs", "II"), ascending=False)`
```
Out[99]: 
               Exams     Labs    
                   I  II    I  II
Student Course                   
Violet  Sci       78  81   81  81
        Math      77  79   81  80
        Comp      76  77   78  79
Quinn   Sci       75  78   78  78
        Math      74  76   78  77
        Comp      73  74   75  76
Ada     Sci       72  75   75  75
        Math      71  73   75  74
        Comp      70  71   72  73
```

# Indexing / selection

The basics of indexing are as follows:
```
Operation               Syntax          Result
-------------------------------------------------
Select column           df[col]         Series
Select row by label     df.loc[label]   Series
Select row by int loc   df.iloc[loc]    Series
Slice rows              df[5:10]        DataFrame
Select rows by boolvec  df[bool_vec]    DataFrame
```

---
---
# Slicing
### Slice columns
```
df.loc[ : , "colA":"colB"]
```

### Scalar from rowid, colname:     
`df['colname'][0]`

j
