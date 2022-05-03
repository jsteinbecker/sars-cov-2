class Student (str):
   @property
   def classof (self):
      return str(self) + " [Class of 2020]"
   
J = Student("Josh")
J == "Josh"

