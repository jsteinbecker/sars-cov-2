

_Filter DF_:
`filterdf = df [df ['col'] == value]`

_New Column from Old_:
`df['newcol'] = df['oldcol'] *Expressions`
> `df['partial year'] = df['year'] + (df['week']/ 52)`

_If-then Column_:
`df.loc[df.AAA >= 5, "BBB"] = -1`
 . | AAA | BBB  |CCC
--|----|------|-----
0    |4  | 10  |100
1    |5   |-1 |  50
2    |6   |-1  |-30
3|   |7   |-1 | -50
