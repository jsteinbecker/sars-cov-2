def reversDict (Dict:dict):
   """ REVERSE DICTIONARY
   ==========================
   Make the values of a dict the new keys
   >>> Dict
   ---------------------------------------
   example:
   {a:1,  b:2,  c:3} ==> {1:a,  2:b,  3:c}
   --------------------------------------- 
   """
   
   return {s[1]:s[0] for s in Dict.items()}