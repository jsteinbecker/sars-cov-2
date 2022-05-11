# %%
#import functions.math as math
import sympy as sp
from IPython.display import display, Markdown



def solveEq(equation,  solvefor,   displayTable=True) -> display :
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
    
def mortgagepayment(P, apr, yrs) -> float :
   """----MORTGAGE PAYMENT--------------------------------
                                  --> MONTHLY PAYMENT IN $
   -------------------------------------------------------
      >>> P     : principle
      >>> apr   : decimal APR
      >>> yrs   : length of term in years
   ======================================================
   """

   r = apr / 12      # MONTHLY PERC. RATE
   n = yrs * 12      # NUMBER OF MONTHS/ TERM

   mp = round(P * r * ((r+1)**n) / ((r+1)**n-1), 2)
   #print (f'Monthly Payment:\t\t${mp}')
   return mp
   #-----------------------------------------------------

class EQN:
   class MonthlyPayment:
      """---Monthly Payment----------------------------
      
         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
         >>> P     PRINCIPLE
         >>> r     RATE/APR
         >>> n     NO. OF MONTHS
         >>> mp    MONTHLY PAYMENT 
         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
      =================================================
      """
      P, r, n, mp = sp.symbols("P r n [PAY_{mo}]")

      equation = sp.Eq(mp, P * r * (((1 + r) ** n) / ((1 + r) ** n - 1)))

      def solveMP(Principle, rate:float, n_months:int, display=0):
         """ 
         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
         >>> Principle      $$ of Loan
         >>> rate           APR as decimal # (0.01 = 1%)
         >>> n_months       No. of Months of Term
         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
         """
         eq = EQN.MonthlyPayment.equation
         s = EQN.MonthlyPayment
         mp = EQN.MonthlyPayment.mp

         f = eq.subs({s.P: Principle,   s.n: n_months,  s.r: rate})

         if display == 0:
            return round(sp.solve(f, s.mp)[0], 2)
         else:
            return f

class EQ_pH (EQN):
   pH, H3O = sp.symbols("pH [H_{3}O]")
   symbols = pH, H3O
   equation = sp.Eq(pH , -sp.log(H3O,10))
   def solve_pH (self, pH):
      return sp.solve(EQ_pH.equation.subs({EQ_pH.pH:pH}),EQ_pH.H3O)

class s :
      pH, pOH = sp.symbols("pH pOH")

class EQ_pH_POH (EQ_pH):
   symbols = s.pH, s.pOH
   equation = sp.Eq(s.pH + s.pOH , 14)
   def solve (pH_in=s.pH,pOH_in=s.pOH):
      return EQ_pH_POH.equation.evalf(subs={s.pH:pH_in,s.pOH:pH_in})

def roundUpToMultiple(number: float, multiple: int) -> int:
    """
    RETURNS VALUE ROUNDED TO A NEAREST MULTIPLE 
    >>> number
    >>> multiple    to round up to
    ======================================================
    
    (Reduces sig figs by factor of provided multiple when 
    multiple is a factor of 10)
    ------------------------------------------------
    Example: 
        Multiple of 100
        >>> 12501 --> 12600
        >>> 12500 --> 12500
        
    ================================================= 
    """

    rounded = number + (multiple - 1)
    return int(rounded - (rounded % multiple))


# %% [markdown]
# # The pH Equation
# 

# %% [markdown]
# ####  Calculate the concentration of protons in a solution with $pH = 7$

# %%
eq = EQ_pH    
eq.equation._has

# %%
sub = eq.equation.subs({eq.pH: 7})
EQ_pH.solve_pH(eq.equation, 10)[0]

# %% [markdown]
# #### Calculate the pOH of a solution with $pH = 2.2$

# %%
eq = EQ_pH_POH
eq.equation

# %%
"Not working??"
eq.solve()


# %%



