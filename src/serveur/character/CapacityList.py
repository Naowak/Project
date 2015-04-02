import Capacity

class CapacityList :
	"""Class which define the list of capacity of a character"""

	def __init__(self) :
		self._list = list()

	def capacityAppend(self, capacity) :
		self._list.append(capacity.clone())

	def capacityRemove(self, capacity) :
		self._list.remove(capacity.clone())

	def clone(self) :
		cl = CapacityList()
		for elem in self._list :
			CapacityList.capacityAppend(elem.clone())
		return cl
