def gcContent (seq):
   seq = seq.lower()
   gcPerc =round((seq.count("g")+seq.count("c")) / len(seq),4)
   return gcPerc

