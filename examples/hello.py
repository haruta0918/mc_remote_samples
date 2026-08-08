from mc_remote.minecraft import Minecraft
import param_mc_remote as param
from param_mc_remote import PLAYER_ORIGIN as PO
from param_mc_remote import block
mc = Minecraft.create(address=param.ADRS_MCR, port=param.PORT_MCR)
mc.setPlayer(param.PLAYER_NAME, PO.x, PO.y, PO.z)


#  size=11
# BLOCK=block.SMOOTH_QUARTZ
# X=0
# Y=63
# Z=0
# size=5
# size2=0
# for i in range(size):
#     X=size2
#     for i in range(size):
#         Z=size2
#         for i in range(size):
#             mc.setBlock(X,Y,Z, BLOCK)
#             print(X,Y,Z)
#             Z+=1
#         X+=1
#     Y+=1
#     size-=2
#     size2+=1
z=-48
y=63
x=-48
for i in range(120):
    z=-48
    for i in range(96):
        x=-48
        for i in range(96):
            mc.setBlock(x,y,z, block.SMOOTH_QUARTZ)
            print(x,y,z)
            x+=1
        z+=1    
    y+=1        
z=-47
y=63
x=-47
for i in range(119):
    z=-47
    for i in range(94):
        x=-47
        for i in range(94):
            mc.setBlock(x,y,z, block.LIGHT)
            print(x,y,z)
            x+=1
        z+=1    
    y+=1               
