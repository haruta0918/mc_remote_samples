from mc_remote.minecraft import Minecraft
import param_mc_remote as param
from param_mc_remote import PLAYER_ORIGIN as PO
from param_mc_remote import block
from litemapy import Schematic, Region 
from litemapy import Schematic

mc = Minecraft.create(address=param.ADRS_MCR, port=param.PORT_MCR)
mc.setPlayer(param.PLAYER_NAME, PO.x, PO.y, PO.z)
  
file_path = "images\ピラミッド.litematic"
schem = Schematic.load(file_path)

print(block)
for region in schem.regions.values():
    block = region.getblock(0,0,0)  
    print("ブロック")
    print(block.id)
# Save the schematic
schem.save("planet.litematic")
# Load the schematic and get its first region
schem = Schematic.load("planet.litematic")
reg = list(schem.regions.values())[0]
# Print out the basic shape
x=0
y=0
z=0

block = region.getblock(0, 0, 0) 
print(block)
mc.setBlock(0, 70, 0, block.id)
print(x,y,z)
# for x in range(schem.width):
#     for y in range(schem.height):
#         for z in range(schem.length):
#             print(x,y,z)
#             block = region[x, y, z] 
#             mc.setBlock(x, y, z, block.id)
            

               

        
