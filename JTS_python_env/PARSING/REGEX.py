import pandas as pd

BASICS = {
   'Start of Line' : '^' ,
   'End of Line'   : '$' ,
   'Digit'         : '\d',
   'Non-Digit'     : '\D',
   'Alnum'         : '\w'
}

FUNCTIONALS = {
   'Zero or more' : '*',
   'One or more'  : '+'
}

GROUPS = {
   'Any of Group' : '[ABC]',
   'Or Group' : 'D|E'
}

pd.Series (BASICS)
pd.Series (FUNCTIONALS)
pd.Series (GROUPS)

