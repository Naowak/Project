class Capacity :
	"""Class which define the capacity of a Character"""

	def __init__(self, fonction, nb, boolean) : #pointeur sur fonction, int pour portee, boolean pour ldv
		self._fct = fonction
		self._portee = nb
		self._ldv = boolean

	def doCapacity(self, *arg) :
		self._fct(arg)

	def getPortee() :
		return self._portee

	def getLdv() :
		return self._ldv

	def setPortee(nb) :
		self._portee = nb

	def setLdv(boolean) :
		self._ldv = boolean

	def clone() :
		return Capacity(self._fct, self._portee, self._ldv)