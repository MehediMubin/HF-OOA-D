import time

class Remote:
   def __init__(self, door):
      self.door = door
      
   def pressButton(self):
      print("Pressing the remote control button...")
      if self.door.isOpen():
         self.door.close_door()
      else:
         self.door.open_door()