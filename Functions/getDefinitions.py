import re

def get_definitions (filename, filecontent):
      """
   ========================================================================================
   
   FOR PROVIDED FILE, FUNCTION WILL EXTRACT DEFINITIONS CONTAINED.
   'DEFINITIONS' FIT THE PATTERN:
   
   
         'TERM'  ::    'DESCRIPTION'
         
   ========================================================================================
      """
   
      lines = filecontent.split("\n")
   
      termDescriptPair = []
      for line in lines:
            if re.findall ("[\w\W]* :: [\w\W]*", line) != []:
                  termDescriptPair.append(line)
      allterms = []
      for t in termDescriptPair:
            trm, des = t.split("::")
            term = trm.strip()
            descrip = des.strip()
            allterms.append ({"term": term,
                              "description": descrip,
                              "source": filename})  

      return allterms

