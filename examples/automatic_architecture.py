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
X1, Y1, Z1 = 0, 0, 0
X2, Y2, Z2 = 0, 0, 0
# Print out the basic shape
for z in reg.zrange():
    X1, Y1, Z1 = 0, 0, 0
    Z2+=size  
    for y in reversed(list(reg.yrange())):
        Y2-=size
        for x in reg.xrange(): 
            b = reg.getblock(x, y, z)
            X1=0
            X2+=size
            for i in range(size):
                Y1=0
                for i in range(size):
                    Z1=0
                    for i in range(size): 
                        mc.setBlock(X1+X2, Y0 +Y1+Y2,Z1+Z2, b.id)
                        print(X1+X2, Y0 +Y1+Y2,Z1+Z2, b.id)
                        sleep(0.01)
                        Z1 +=1  
                    Y1 +=1
                X1 +=1
        X2=0
    Y2=0                


