
class DogDoor:
   def __init__(self):
      self.open = False
      
   def open_door(self):
      print('The dog door opens')
      self.open = True
      
   def close_door(self):
      print('The dog door closes')
      self.open = False
      
   def isOpen(self):
      return self.open