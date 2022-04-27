from classes import *

Patients = [
   makePatient("Josh",27,72,74,0.92),
   makePatient("Fred",68,82,100,1.92)
]


patients_txt = open("00 PK/patients.txt","w")
out = "PATIENTS:\n"
out += "* "*32 + "\n"
for pt in Patients:
   out += str(pt)
   out += "\n"
patients_txt.write(out)
patients_txt.close()