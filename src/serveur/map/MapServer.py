import TileServer
import random

MAP_SIDE_X = 50
MAP_SIDE_Y = 50

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


				



