s = [["mi","7c","  "],
     ["7c","  ","  "],
     ["7p","  ","mi"] ]

def dayschedule (day):
   ds = []
   for x in s:
      ds.append(x[day])
   return ds

needed = [["mi","7c","7p"],
          ["mi","7c","7p"]]

def needsmet (day):
   gds = dayschedule(day)
   isin = []
   for x in needed:
      i = x in gds
      isin.append(i)
   nm = all(isin)
   return nm

needsmet (0)