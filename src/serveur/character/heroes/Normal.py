import sys
sys.path.append("../")
sys.path.append("../../")
sys.path.append("../../mapping/")
from Character import Character
import CapacityList
import Capacity
import VG


def attaque(coord) :
	if(not VG.grid.isTileBloc(coord) and not VG.grid.isTileHole(coord)) :
		c = VG.grid.getCharacter(coord)
		print(coord)
		print(c)
		if(c != None) :
			c.setLifePoint(c.getLifePoint() - 5)

fctAttaque = Capacity.Capacity("attaque", attaque, 0, False)


class Normal(Character) :
	"""Class which define a normal classic hero for test"""

	def __init__(self, name) :
		super(Normal, self).__init__(name)
		self.setCapacity(fctAttaque)
