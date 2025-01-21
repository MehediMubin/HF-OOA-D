from DogDoor import DogDoor
from Remote import Remote
from BarkRecognizer import BarkRecognizer
import time

door = DogDoor()
recognizer = BarkRecognizer(door)
remote = Remote(door)

print("Fido start barking...");
recognizer.recognize("Woof")
# remote.pressButton()

print("Fido has gone outside...")
print("Fido's all done...")
time.sleep(10)

print("But he's stuck outside")
print("Fido start's barking")
recognizer.recognize("Woof")

# print("So, Gina grabs the remote control")
# remote.pressButton()
print("Fido's back inside...")