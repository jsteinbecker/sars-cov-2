# %%
program_title = """\
===============================================
DATE BACTRIM 
-----------------------------------------------
(SULFAMETHOXAZOLE/TRIMETHOPRIM) 
FOR IV USE IN 
DEXTROSE 5% WATER
===============================================
"""


def date_bactrim(bag_mL, drug_mL=0, drug_mg=0):
   if drug_mg == 0 :
      if drug_mL == 0:
         return "Error: Add either drug_mL or drug_mg"
   if drug_mg != 0 : 
      if drug_mL != 0:
         if drug_mL / 16 != drug_mg:
            return "Error: Mismatched Drug_mL / mg. Stock Sol  = 16mg/mL..."
   if drug_mg == 0:
      drug = drug_mL  
   if drug_mL == 0:
      drug = drug_mg / 16 #mg/mL
   bag = bag_mL

   tmp = drug 
   total_vol = drug + bag
   conc = round(tmp / total_vol, 2)

   return str(conc) + "mg TMP/mL"
date_bactrim(500,drug_mg=220)
single_line = "-----------------------------------------------"
double_line = "==============================================="


def main():
   print (program_title)
   drug = int(input("VOLUME OF STOCK SMZ/TMP (ML): "))
   bag  = int(input("VOLUME OF IVPB D5W BAG  (ML): "))
   answer = date_bactrim(drug,bag)
   print (single_line)
   print (answer)
   print (double_line)

if __name__ == '__main__':
   main()

  
# %%
