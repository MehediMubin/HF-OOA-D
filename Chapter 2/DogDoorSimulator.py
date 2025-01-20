from DogDoor import DogDoor
from Remote import Remote
import time

door = DogDoor()
remote = Remote(door)

print("Fido barks to go outside...");
remote.pressButton()
print("Fido has gone outside...")
print("Fido's all done...")
time.sleep(10)
print("But he's stuck outside")
print("Fido start's barking")
print("So, Gina grabs the remote control")
remote.pressButton()
print("Fido's back inside...")