from time import sleep

from litemapy import Schematic, Region, BlockState

from mc_remote.minecraft import Minecraft
import param_mc_remote as param
from param_mc_remote import PLAYER_ORIGIN as PO
from param_mc_remote import block

# Connect to minecraft and open a session as player with origin location
mc = Minecraft.create(address=param.ADRS_MCR, port=param.PORT_MCR)
mc.setPlayer(param.PLAYER_NAME, PO.x, PO.y, PO.z)

mc.postToChat("LITEMAPY!!")


# file_name = "sample.litematic"
file_name = "images/ファンタジー建築１.litematic"
X0, Y0, Z0 = 0, 62, 0

# Load the schematic and get its first region
schem = Schematic.load(file_name)
reg = list(schem.regions.values())[0]

# Print out the basic shape
for z in reg.zrange():
    for y in reversed(list(reg.yrange())):
        for x in reg.xrange():
            b = reg.getblock(x, y, z)
            mc.setBlock(X0 + x, Y0 + y, Z0 + z, b.id)
            print(X0 + x, Y0 + y, Z0 + z, b.id)
            sleep(0.001)