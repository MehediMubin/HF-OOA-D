from enum import Enum

class Type(Enum):
   ACOUSTIC = "Acoustic"
   ELECTRIC = "Electric"
   
   def __str__(self):
      return self.value