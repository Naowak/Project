FREE = 0
HOLE = 1
BLOC = 2
TAKEN = 3

class TileServer :
	"""Class which define the map's tile on the Server side"""

	def __init__(self) :
		self._tile = FREE
		self._charactere = None

	def isTileFree(self) :
		return self._tile == FREE

	def isTileHole(self) :
		return self._tile == HOLE

	def isTileBloc(self) :
		return self._tile == BLOC

	def isTileTaken(self) :
		return self._tile == TAKEN

	def getCharactere(self) : 
		return self._charactere

	def setTileFree(self) : 
		self._tile = FREE

	def setTileHole(self) :
		self._tile = HOLE

	def setTileBloc(self) :
		self._tile = BLOC

	def setTileTaken(self, c) :
		self._tile = TAKEN
		self._charactere = c

	def __str__(self) :
		if(self.isTileFree()) :
			return "_"
		if(self.isTileHole()) :
			return "."
		if(self.isTileBloc()) :
			return "M" 
		if(self.isTileTaken()) :
			return "O"
