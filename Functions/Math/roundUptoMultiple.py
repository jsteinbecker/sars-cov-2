def roundUpToMultiple(number:float, multiple:int) -> int:
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

def accumulate (Set, specialReturn= None) -> list:
   """_summary_
            Running Total Accumulation 
            of List of numbers

      >>> Set = [2, 3,  7, 12, 14, 16, 2]
      >>> accumulate(Set)
                [2, 5, 12, 24, 38, 54, 56]
   ---------------------------------------
   """
   accum = [0]
   
   for x in Set:
      new = accum[-1] + x
      accum.append(new)
      
   if specialReturn == 'md':
      md_str = ""
      for x in range(len(Set)):
         ob = '{'; cb = '}'
         md_str += f'\\xrightarrow{ob}+{Set[x]}{cb} {accum[x+1]}'
      
      md = "$" + md_str + "$"
      
      return Markdown(md)
   else:
      pass
   
   if specialReturn == None:
      return accum[1:] 

def rtmult() -> int:
    """ROUNDS NUMBER TO A SPECIFIED MULTIPLE"""
    
    number = float(input("Value: "))
    multiple = int(input("Multiple: "))

    rounded = roundUpToMultiple(number,multiple)
    return rounded

