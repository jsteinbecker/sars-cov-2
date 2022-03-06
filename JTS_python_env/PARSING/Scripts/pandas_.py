import pandas as pd
data = {
      ("AGS","amikacin") : [ 0 , 55 , 99 , 2], 
      ("AGS","gentamicin") : [22 , 67 , 99 , 98],
      ("ßLac","Amox-Clav") : [55 , 56 , 9 , 0],
      ("ßLac","Unasyn") : [44, 89 , 78 , 0],
      ("AGS","Unasyn") : [9, 6 , 7 , 8]
      }
df = pd.DataFrame(data)

def get_column (col_name):
   return df[col_name]


def get_col_from_id (col_id):
   return df.iloc [col_id]


def df_summary_stats (df):
   return df.describe ()

def get_subcolumn (col_name, subcol_name):
   out = df [col_name][subcol_name]
   return out

def group_columns (df, tuple_col):
   """
   >>> df
      A           B           C           D
      x   y   z   x   y   z   x   y   z   x   y   z
   T                                               
   0   1   2   1   3   2   1   4   2   1   5   2   1
   1   8   2   3   3   2   9   9   1   3   4   9   1
   2   4   5   7   7   7   1   8   3   6   9   2   3
   ===================================================
   """
   import pandas as pd

   df.columns = pd.MultiIndex.from_tuples ([(tuple_col[0], tuple_col[1]) for tuple_col in df.columns])
   return df

def group_columns_example ():
   import pandas as pd

   data = {
      ("AGS","amikacin") : [ 0 , 55 , 99 , 2], 
      ("AGS","gentamicin") : [22 , 67 , 99 , 98],
      ("ßLac","Amox-Clav") : [55 , 56 , 9 , 0],
      ("ßLac","Unasyn") : [44, 89 , 78 , 0],
      ("AGS","Unasyn") : [9, 6 , 7 , 8]
      }
   df = pd.DataFrame(data)
   df.index = ["S. pyogenes" , "S. aureus (MRSA)" , "Klebsiella spp." , "E. coli"]
   return df
group_columns_example()

