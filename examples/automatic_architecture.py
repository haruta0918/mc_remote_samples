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
file_name = "images/ピラミッド.litematic"
# file_name = "images/Sample2.litematic"
X0, Y0, Z0 = 0, 90, 0
sleep(2)
# Load the schematic and get its first region
schem = Schematic.load(file_name)
reg = list(schem.regions.values())[0]
size = 1 
# x2, y2, z2 とかも、sizeと同期させる
x1, y1, z1 = 0, 0, 0
x2, y2, z2 = 0, 0, 0
# Print out the basic shape
for z in reg.zrange():
    x1, y1, z1 = 0, 0, 0
    z2+=size  
    for y in reversed(list(reg.yrange())):
        y2-=size
        for x in reg.xrange():
            b = reg.getblock(x, y, z)
            x1=0
            x2+=size
            for i in range(size):
                y1=0
                for i in range(size):
                    z1=0
                    for i in range(size): 
                        mc.setBlock(x1+x2, Y0 +y1+y2,z1+z2, b.id)
                        print(x1+x2, Y0 +y1+y2,z1+z2, b.id)
                        sleep(0.01)
                        z1 +=1  
                    y1 +=1
                x1 +=1
        x2=0
    y2=0                


