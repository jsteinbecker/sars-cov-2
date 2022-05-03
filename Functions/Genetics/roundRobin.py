from tokenize import group


N = 203
n_groups = 15
def split_into_groups (N,n_groups):
   """SPLIT INTO GROUPS
   ====================
   >>> N          : number of individuals
   >>> n_groups   : number of groups
   """
   i_per_group       = N // n_groups
   i_remainder       = N %  n_groups
   g_1groups         = [i_per_group+1] * i_remainder
   g_0groups         = [i_per_group]   * (n_groups - i_remainder)
   
   groups = [*g_1groups, *g_0groups]
   return groups

split_into_groups (N,n_groups)

group_names = ["group" + str(i) for i in range(n_groups)]

import itertools as itr
list(itr.cycle(group_names))