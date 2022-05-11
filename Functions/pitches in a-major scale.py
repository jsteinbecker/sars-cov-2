import numpy as np

def a_n ():
  """fx: returns a list of ints"""
  
  # values:
  oct1      = 440        #hz
  oct2      = oct1 * 2   #(880 hz)
  steps     = 12         #per octave

  n = np.linspace(oct1, oct2, steps)
  return n

print(a_n())
             #W W H W W W H
majorscale = [2,2,1,2,2,2,1]

ct = 0
out = []
out.append(a_n()[0])
for x in majorscale:
  ct += x
  out.append(a_n()[ct])
  
len(out)