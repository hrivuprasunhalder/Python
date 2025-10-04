from jackrussellterrier import JackRussellTerrier
from dachshund import Dachshund
from bulldog import Bulldog
dog1=JackRussellTerrier("Miles",4)
dog2=Dachshund("Buddy",9)
dog3=Bulldog("Jack",5)
dog4=Bulldog("Jimbo",3)

print(dog1.species)
print(dog2.species)
print(dog3.species)
print(dog4.species)
print(f"The name of the first dog is {dog1.name}")
print(f"The 2nd dog is {dog2.name}")
print(dog3)
dog4.speak("Woof")
print(isinstance(dog1,JackRussellTerrier))
print(isinstance(dog2,JackRussellTerrier))
# print(isinstance(dog1,Dog)) will be true,but importing parent class is necessary in that case
