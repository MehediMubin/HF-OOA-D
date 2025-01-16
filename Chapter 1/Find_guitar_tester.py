from Inventory import Inventory
from Guitar import Guitar
from Builder import Builder
from Type import Type
from Wood import Wood
from Guitar_Spec import GuitarSpec


MyInventory = Inventory()

MyInventory.add_guitar("123", 23.22, GuitarSpec(Builder.FENDER, "stratocastor", Type.ELECTRIC, "6-string", Wood.ALDER, Wood.ALDER))

MyInventory.add_guitar("1245", 100.343, GuitarSpec(Builder.FENDER, "stratocastor", Type.ELECTRIC, "6-string", Wood.ALDER, Wood.ALDER))


whatErinLikes = GuitarSpec(Builder.FENDER, "Stratocastor", Type.ELECTRIC, "6-string", Wood.ALDER, Wood.ALDER)

matchingGuitars = MyInventory.search(whatErinLikes)
   
if matchingGuitars:
   print("Erin, you might like these guitars!")
   for guitar in matchingGuitars:
      spec = guitar.get_spec()
      print(f"We have a {spec.get_builder()} {spec.get_model()} {spec.get_type()} guitar with {spec.get_back_wood()} back and sides {spec.get_top_wood()} and you can have it for only ${guitar.get_price()}")
else:
   print("Sorry, Erin, we have nothing for you!")