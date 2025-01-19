from DogDoor import DogDoor
from Remote import Remote

door = DogDoor()
remote = Remote(door)

print("Fido barks to go outside...");
remote.pressButton()
print("Fido has gone outside...")
remote.pressButton()
print("Fido's all done...")
remote.pressButton()
print("Fido's back inside...")
remote.pressButton()