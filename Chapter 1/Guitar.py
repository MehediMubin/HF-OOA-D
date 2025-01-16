
class Guitar:
  def __init__(self, serial_number, price, spec):
    self.serial_number = serial_number
    self.price = price
    self.spec = spec
    
  def get_serial_number(self):
    return self.serial_number
  
  def get_price(self):
    return self.price
  
  def set_price(self, price):
    self.price = price
    
  def get_spec(self):
    return self.spec
  
  def __str__(self):
    spec = self.get_spec()
    return f"We have a {spec.get_builder()} {spec.get_model()} {spec.get_type()} with {spec.get_back_wood()} back and sides {spec.get_top_wood()} and you can have it for only ${self.get_price()}"