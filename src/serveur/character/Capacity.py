class Capacity :
	"""Class which define the capacity of a Character"""

	def __init__(self, name, fonction, nb, boolean) : #pointeur sur fonction, int pour portee, boolean pour ldv
		self._name = name
		self._fct = fonction
		self._portee = nb
		self._ldv = boolean

	def doCapacity(self, coord) : #demande un dict
		self._fct(coord)

	def getPortee(self) :
		return self._portee

	def getLdv(self) :
		return self._ldv

	def getName(self) :
		return self._name

	def setPortee(self, nb) :
		self._portee = nb

	def setLdv(self, boolean) :
		self._ldv = boolean

	def clone(self) :
		return Capacity(self._name, self._fct, self._portee, self._ldv)

	def __str__(self) :
		return str(self._fct) + " " + str(self._portee) + " " + str(self._ldv)