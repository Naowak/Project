import Capacity

class CapacityList :
	"""Class which define the list of capacity of a character"""

	def __init__(self) :
		self._list = list()

	def capacityAppend(self, capacity) :
		self._list.append(capacity)

	def capacityRemove(self, capacity) :
		self._list.remove(capacity)

	def getCapacityList(self) :
		l = list()
		for elem in _list :
			l.append(elem.clone())
		return l

	def clone(self) :
		cl = CapacityList()
		for elem in self._list :
			cl.capacityAppend(elem.clone()) #Attention, la capacité est cloné, ce n'est pas la même référence !
		return cl

	def __str__(self) :
		string = ''
		for elem in self._list :
			string += str(elem) + " / "
		return string