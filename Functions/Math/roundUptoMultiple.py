def roundUpToMultiple(number:float, multiple:int) -> int:
    """RETURNS VALUE ROUNDED TO A NEAREST MULTIPLE 
    
    (REDUCES SIG FIGS BY FACTOR OF PROVIDED MULTIPLE
    WHEN MULTIPLE IS A FACTOR OF 10)"""

    rounded = number + (multiple - 1)
    return int(rounded - (rounded % multiple))



def rtmult() -> int:
    number = float(input("Value: "))
    multiple = int(input("Multiple: "))

    rounded = roundUpToMultiple(number,multiple)
    
    return rounded
