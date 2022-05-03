
from regex import E


def example (): 
   'Underscores dont mess with int values'
   n_1 = 2_000_000
   n_2 = 3_500_000
   print(n_1,str(n_1))
   print(n_2,str(n_2))

def commas (number):
   'f-string comma int formatter'
   return f'{number:,}'

