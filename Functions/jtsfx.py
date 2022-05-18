from IPython.display import Markdown
import sympy as sp
from matplotlib import rcParams
import base64
from IPython.display import Image, display
import matplotlib.pyplot as plt

# FUNCTIONS FOR DISLAY SETTINGS

def add_MD_Dollars_              (math_string) -> str: 
   return "$" + math_string + "$"


def add_MD_Dollars_Display_      (math_string) -> Markdown:  
   return Markdown(add_MD_Dollars_(math_string))


def solveEq                      (equation,  solvefor,   displayTable=True) -> Markdown :
   """
   |--MARKDOWN DISPLAY FUNCTION--------------------|
   
      SOLVE SYMPY EQUATION, DISPLAYS BOXED ANSWER  
   |===============================================|
   |
   |        >>> 1. equation    : sympy
   |        >>> 2. solveFor    : sp.Symbol
   |      
   |        >>> *3. displayTable   = True
   |_______________________________________________|
   """

   try:
      # GOOD RESPONSE ASSUMING SP PUT SOLUTION IN LIST
      s = sp.solve(equation, solvefor)[0]
   except:
      return "UNSOLVABLE"
   eq = sp.Eq(solvefor, s)

   #display (Markdown("$~~~~~~~~~~\\boxed{"+eq._repr_latex_().replace("$","")+"}$"))
   if displayTable == True:
      solved = "$\\boxed{"+eq._repr_latex_().replace("$", "")+"}$"
      equa = eq._repr_latex_()
      table = f'Equation | *Solve for {solvefor._repr_latex_()} :*\n---|---------\n{equation._repr_latex_()} | {solved}'
      MD = Markdown(table)

      return display(MD)
   
   else:
      pass
   #===========================================
   
def makespSymbols(symbol):
   return [sp.Symbol(x) for x in symbol.split(" ")]

def sp_PrintAll ():
   sp.printing.str.StrPrinter._default_settings['abbrev'] = True

def derivative (func):
   dfdx = sp.diff (func)
   return dfdx

def showDerivative (func):
   dfdx = derivative(func)
   display(func)
   str_ddx = "$ \\frac {d}{dx} = <<>>"
   ddx = str_ddx.replace("<<>>", dfdx._repr_latex_())
   output = ddx.replace("$\\displaystyle", "")
   display(Markdown(output))
   
   
def snsFigSize (w,h):
   rcParams['figure.figsize'] = w, h
   

# %%
def mermaid (graph, darkmode=1) -> Image:
  if darkmode == 1:
    graph = "%%{init: {'theme': 'dark'}}%%" + graph
  graphbytes = graph.encode("ascii")
  base64_bytes = base64.b64encode(graphbytes)
  base64_string = base64_bytes.decode("ascii")
  display(Image(url="https://mermaid.ink/img/" + base64_string))
# %%
