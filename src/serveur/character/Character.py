import CapacityList

class Character :
	"""Class which define a character on the Server side"""

	def __init__(self, name) :
		self._name = name
		self._lifePointMax = None
		self._lifePoint = self._lifePointMax
		self._manaMax = None
		self._mana = self._manaMax
		self._speedMax = None
		self._speed = self._speedMax
		self._capacity = CapacityList.CapacityList() 

	def __str__(self) :
		return "< " +  self.getName() + " > : LPM : " + str(self.getLifePointMax()) + ", LP : " + str(self.getLifePoint()) + ", mM : " + str(self.getManaMax()) + ", m : " \
		+ str(self.getMana()) + ", SM : " + str(self.getSpeedMax()) + ", S : " + str(self.getSpeed()) + ", CL : " + str(self.getCapacity())

	def clone(self, name) :
		c = Character(name)
		c.setLifePointMax(self._lifePointMax)
		c.setLifePoint(self._lifePoint)
		c.setManaMax(self._manaMax)
		c.setMana(self._mana)
		c.setSpeedMax(self._speedMax)
		c.setSpeed(self._speed)
		c.setCapacityList(self._capacity)
		return c

	def getName(self) :
		return self._name
	
	def setCapacityList(self, capacityList) :
		self._capacity = capacityList.clone()

	def getLifePointMax(self) :
		return self._lifePointMax

	def setLifePointMax(self, nb) :
		self._lifePointMax = nb

	def getLifePoint(self) :
		return self._lifePoint

	def setLifePoint(self, nb) :
		self._lifePoint = nb

	def getManaMax(self) :
		return self._mana

	def setManaMax(self, nb) :
		self._manaMax = nb

	def getMana(self) :
		return self._mana

	def setMana(self, nb) :
		self._mana = nb

	def getSpeedMax(self) :
		return self._speedMax

	def setSpeedMax(self, nb) :
		self._speedMax = nb

	def getSpeed(self) :
		return self._speed

	def setSpeed(self, nb) :
		self._speed = nb

	def getCapacity(self) :
		return self._capacity.clone()

	def setCapacity(self, capacity) :
		self._capacity.capacityAppend(capacity)

	def removeCapacity(self, capacity) :
		self._capacity.capacityRemove(capacity)