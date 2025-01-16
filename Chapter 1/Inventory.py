from Guitar import Guitar
from Guitar_Spec import GuitarSpec

class Inventory:
  def __init__(self):
    self.guitars = []
    
  def add_guitar(self, serial_number, price, guitar_spec):
    guitar = Guitar(serial_number, price, guitar_spec)
    self.guitars.append(guitar)
    
  def get_guitar(self, serial_number):
    for guitar in self.guitars:
      if guitar.serial_number == serial_number:
        return guitar
      
    return None
 
 
  def search(self, search_spec):
     matching_guitars = []
     for guitar in self.guitars:
        if guitar.get_spec().matches(search_spec):
           matching_guitars.append(guitar)
      
     return matching_guitars
  
  
  def __str__(self):
      return "Thish ish my In-the-ven-the-tory"   