def gcContent (seq):
   """
   Function: Return GC Content of Nucleic Acid Sequence. Returned as decimal value. 
   """
   seq = seq.lower()

   gcPerc = round((seq.count("g")+seq.count("c")) / len(seq),4)

   return gcPerc

