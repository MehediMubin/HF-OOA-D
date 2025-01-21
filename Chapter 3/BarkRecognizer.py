

class BarkRecognizer:
   def __init__(self, door):
      self.door = door
      
   def recognize(self, bark):
      print(f"BarkRecognizer: Heard a {bark}")
      self.door.open_door()