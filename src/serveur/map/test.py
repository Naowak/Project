from MapServer import *
from Coord import *


map = MapServer()
print(map)

x = Coord(2, 4)
y = Coord(3, 4)
z = Coord(1, 4)
a = Coord(4, 4)
b = Coord(0, 4)

map.setTileFree(x)
map.setTileHole(y)
map.setTileBloc(z)
map.setTileTaken(a, 5)

print(map.isTileFree(x), map.isTileFree(y))
print(map.isTileHole(y), map.isTileHole(x))
print(map.isTileBloc(z), map.isTileBloc(a))
print(map.isTileTaken(a), map.isTileTaken(z))
print(map.getCharacter(a), map.getCharacter(z))