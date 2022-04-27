
def remove_MDTable_Bar (text:str) -> str:
   """
   Remove Markdown Table --|--|--...
   ------------------------------------
   Returns Full Text passed, removing the `---|---...` Line
   >>> pattern= "\\n(\s*-+\|-+\s*)+(?=\\n)"

   --------------------------------------------------------------"""
   import re
   pattern = "\n(\s*-+\|-+\s*)+(?=\n)"
   repl = ""

   edit = re.sub(pattern,repl,text)
   return edit



def pipe_to_comma (text:str) -> str:
   """
   Pipe To Comma (MDTable Convert)
   -------------------------------
   """
   import re
   pattern = "\|\s"
   repl = ", "

   edit = re.sub(pattern,repl,text)
   return edit


