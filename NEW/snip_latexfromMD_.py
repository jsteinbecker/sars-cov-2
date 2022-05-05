import re

def extract_md_quotes (file_path):
   """
   -----------------------
   EXTRACT MARKDOWN QUOTES      
   -----------------------
      Example text text...
   >>> ``` quote
   >>> This will be extracted.
   >>> ```
   >>>   This will not be.
   
   >>> "This will also be extracted."
   
   ======================================================================================
                                                              Output >>> List (of quotes)
   """
   file_ = open (file_path , "r")
   data = file_.read()

   re_pattern = "(?<=```quote\n).*\n*.*\n*.*(?=\n*```)"
   quotes = re.findall (re_pattern , data)

   print (str(len(quotes)) + " quotes extracted")
   for quote in quotes:
      print(quote)
   return quotes
# Runnng code ---



def extract_md_latex (file_path):

   """
   -----------------------
   |  EXTRACT MARKDOWN LATEX      
   -----------------------
   >>> $$ x = y^2 $$  <-- Extracted
   >>> x = y^3        <-- Not Extracted
   
   ==========================================================================================
                                                              Output >>> List (of latex expr)
   """
   import re

   file_ = open (file_path , "r")
   data = file_.read()

   re_pattern = "\$\$.*\$\$?"
   snipper = re.findall (re_pattern,  data)
   file_.close()

   print (str(len(snipper)) + " quotes extracted:")
   for snip in snipper:
      print (snip)
   return snipper


