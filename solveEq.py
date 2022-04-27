def solveEq(equation, solvefor):
   """
   |--MARKDOWN DISPLAY FUNCTION--------------------|
   |  SOLVE SYMPY EQUATION, DISPLAYS BOXED ANSWER  |
   |===============================================|
   """
   import sympy as sp
   from IPython.display import Markdown, display
   
   
   display(equation)
   display(Markdown("*Solve for " + solvefor._repr_latex_() + ":*"))

   s = sp.solve(equation, solvefor)[0]
   eq = sp.Eq(solvefor, s)

   display(
       Markdown("$~~~~~~~~~~\\boxed{"+eq._repr_latex_().replace("$", "")+"}$"))

   return eq
   #-------------------------------------------------
