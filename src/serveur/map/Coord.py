class Coord :

	def __init__(self, x, y) :
		self._x = x
		self._y = y

	def getX(self) :
		return self._x

	def getY(self) :
		return self._y

	def setX(self, x) :
		self._x = x

	def setY(self, y) :
		self._y = y

	def __str__(self) :
		return "(" + str(self._x) + ";" + str(self._y) + ")"

	def __eq__(self, other) :
		return isinstance(other, self.__class__) and other._x == self._x and other._y == self._y

	def __ne__(self, other) :
		return not self == other