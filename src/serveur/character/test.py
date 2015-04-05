import sys
path = "../mapping/"
sys.path.append(path)
import MapServer
import Capacity
import CapacityList
import Character
from mapping import Coord

def fct(**arg) :
	print("lol\n")

def fct2(**arg) :
	print("douze")

def fct3(**arg) :
	print("plop")

c = Capacity.Capacity(fct, 0, False)
q = Capacity.Capacity(fct2, 8, True)
w = Capacity.Capacity(fct3, 25, False)

y = CapacityList.CapacityList()
y.capacityAppend(c)
y.capacityAppend(q)
x = y.clone()
x.capacityAppend(w)

jean = Character.Character("Hector")
jean.setLifePointMax(5000)
jean.setLifePoint(3005)
jean.setManaMax(100)
jean.setMana(35)
jean.setSpeed(6)
jean.setSpeedMax(8)
print(jean)

herve = jean.clone("henry")

jean.setCapacity(c)
jean.setCapacity(q)
print(jean)
jean.removeCapacity(q)
print(jean)

herve.setCapacityList(y)
print(herve)

coord = Coord.Coord(2, 5)
herve.setLoc(coord)
print(herve)



