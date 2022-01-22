# Define new coloumn
#FORM:
df['newcol'] = df['oldcol'] <<Expression>>

df['partial year'] = df['year'] + (df['week'] / 52)