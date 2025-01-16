
class GuitarSpec:
   def __init__(self, builder, model, type, num_strings, back_wood, top_wood):
    self.builder = builder
    self.model = model
    self.type = type
    self.num_strings = num_strings
    self.back_wood = back_wood
    self.top_wood = top_wood
    
   def get_builder(self):
    return self.builder
  
   def get_model(self):
    return self.model
  
   def get_type(self):
    return self.type
  
   def get_num_strings(self):
      return self.num_strings
   
   def get_back_wood(self):
    return self.back_wood
  
   def get_top_wood(self):
    return self.top_wood
 
   
   def matches(self, other_spec):
      if self.builder != other_spec.builder:
         print("A")
         return False
      if self.model and self.model.lower() != other_spec.model.lower():
         print("B")
         return False
      if self.type != other_spec.type:
         print(self.type, other_spec.type)
         print("C")
         return False
      if self.num_strings != other_spec.num_strings:
         print("D")
         return False
      if self.back_wood != other_spec.back_wood:
         print("E")
         return False
      if self.top_wood != other_spec.top_wood:
         print("F")
         return False
      
      return True
 
   def __str__(self):
      return self.model 