import sympy as sp
import random
from IPython.display import Markdown
import pandas as pd

class Patient:
   """
   ### Class: PATIENT
   ----------------------------------
   *INITS*
   >>> name
   >>> weight
   >>> age
   >>> SerCreat
   """
   
   def __init__(self, name, weight, age, SerCreat, female:bool):
      """### Class: PATIENT
      ***
      """
      self.gendcode = 1
      if female == True:
         self.gendcode = 0.85
      self.name =       name
      self.id =         random.randint(1000000,10000000)
      self.weight =     weight
      self.age =        age
      self.SerCreat =   SerCreat
      self.CrCl = ((140-self.age) * self.weight) / (72 * self.SerCreat)
   
   def as_dict (self):
      return {
         "name":              self.name, 
         "id":                self.id, 
         "weight":            self.weight, 
         "age":               self.age, 
         "SerumCreatinine":   self.SerCreat, 
         "CrCl":              self.CrCl
         }
   
   @property
   def CrCl_show (self):
      name =      self.name
      age =       self.age 
      weight =    self.weight
      scr =       self.SerCreat
      
      a , w , Cr = sp.symbols("a_yr W_kg Cr_Ser")
      CrCl = ((140-a) * w) / (72 * Cr)
      
      # Dependent Var = 
      md1 = "$\large CrCl_{" + name + "} = $" 
      # View Input Subs
      md2 = "$ " + sp.Subs(CrCl,(a,w,Cr),(age,weight,scr))._repr_latex_()[1:] + "$"
      # Solution
      md3 = "$\large = \\boxed {" + str(round(CrCl.subs({a:age,w:weight,Cr:scr}),1)) + "}$"
      
      table = Markdown (f"Solve for | Subs | Solution\n----|----|----\n{md1} | {md2} | {md3}\n")
      
      return table

   def __repr__(self):
      return f'Name: {self.name}\n\tID:{self.id}\n\t{self.weight}kg\n\t{self.age}yr.of age\n\n\tCr(serum): {self.SerCreat}\n\t{self.CrCl}'
