from mc_remote.minecraft import Minecraft
import param_mc_remote as param
from param_mc_remote import PLAYER_ORIGIN as PO
from param_mc_remote import block
mc = Minecraft.create(address=param.ADRS_MCR, port=param.PORT_MCR)
mc.setPlayer(param.PLAYER_NAME, PO.x, PO.y, PO.z)
size=11
x=0-size
y=100
z=0-size
size2=size
for i in range(size2):
    x=0-size
    for i in range(size2):
        z=0-size
        for i in range(size2):
            mc.setBlock(x,y,z, block.DIAMOND_BLOCK)
            print(x,y,z)
            z+=1
        x+=1
    y+=1
    size-=1
    size2-=2 