

def cleanDNA (seq:str) -> str:
   """
   --------------------
   CLEAN DNA STRING
   --------------------
   REMOVES DIGITS, SPACES AND 
   NEWLINE CHARACTERS FROM INPUT
   ----------------------------------
   """
   import re

   seq = re.sub("\d","",seq) #digits
   seq = re.sub("\s","",seq) #spaces
   seq = re.sub("\n","",seq) #newlines
   seq = seq.lower()

   return seq





def main():
   seq = input("sequence: ")
   return cleanDNA(seq)

if __name__ == "__main__":
   print(main())