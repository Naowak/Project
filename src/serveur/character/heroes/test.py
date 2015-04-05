import sys
sys.path.append("../")
sys.path.append("../../")
sys.path.append("../../mapping/")
import Character
import CapacityList
import Capacity
import MapServer
import Coord
import Normal
import VG

print(VG.grid)

coord = Coord.Coord(2, 4)
coord2 = Coord.Coord(2, 0)

jean = Normal.Normal("jean")
jean.setLoc(coord)

hubert = Normal.Normal("Hubert")
hubert.setLoc(coord2)
hubert.setLifePoint(1000)

VG.grid.setTileTaken(coord, jean)
VG.grid.setTileTaken(coord2, hubert)

print(VG.grid)
print(jean)
print(hubert)

jean.doCapacity("attaque", hubert.getLoc())

print(hubert)

