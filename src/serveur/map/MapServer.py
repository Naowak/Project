import TileServer
import random
import Coord

MAP_SIDE_X = 5
MAP_SIDE_Y = 5

class MapServer:
	"""Class which define the map on the Server side"""

	def __init__(self) :
		self._tab = list()
		for j in range(MAP_SIDE_Y) :
			self._tab.append(list())
			for i in range(MAP_SIDE_X) : 
				self._tab[j].append(TileServer.TileServer())
				nbRandom = random.random()
				if(nbRandom < 0.1) :
					self._tab[j][i].setTileBloc()
				elif(nbRandom >= 0.1 and nbRandom < 0.15) :
					self._tab[j][i].setTileHole()
				else :
					self._tab[j][i].setTileFree()

	def __str__(self) :
		str = ""
		for j in range(MAP_SIDE_Y) :
			for i in range(MAP_SIDE_X) :
				str += self._tab[j][i].__str__()
			str += "\n"
		return str

	def getTile(self, coord) :
		return self._tab[coord.getY()][coord.getX()]

	def isTileFree(self, coord) :
		return self.getTile(coord).isTileFree()

	def isTileHole(self, coord) :
		return self.getTile(coord).isTileHole()

	def isTileBloc(self, coord) :
		return self.getTile(coord).isTileBloc()

	def isTileTaken(self, coord) :
		return self.getTile(coord).isTileTaken()

	def getCharacter(self, coord) :
		return self.getTile(coord).getCharacter()

	def setTileFree(self, coord) :
		self.getTile(coord).setTileFree()

	def setTileHole(self, coord) :
		self.getTile(coord).setTileHole()

	def setTileBloc(self, coord) :
		self.getTile(coord).setTileBloc()

	def setTileTaken(self, coord, c) :
		self.getTile(coord).setTileTaken(c)



				



