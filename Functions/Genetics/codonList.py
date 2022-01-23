"""
GENERATOR: CODONS OF 3 NUCLEOTIDES
"""

nt = 'acgt'
nts = []

for x in nt:
   for y in nt:
      for z in nt:
         nts.append(x+y+z)

nts