# from mc_remote.minecraft import Minecraft
# import param_mc_remote as param
# from param_mc_remote import PLAYER_ORIGIN as PO
# from param_mc_remote import block
# from litemapy import Schematic 

# mc = Minecraft.create(address=param.ADRS_MCR, port=param.PORT_MCR)
# mc.setPlayer(param.PLAYER_NAME, PO.x, PO.y, PO.z)
  
# file_path = "images\ピラミッド.litematic"
# schem = Schematic.load(file_path)


# for region in schem.regions.values():
#     block1 = region.getblock(0,0,0)  


# schem.save("planet.litematic")

# schem = Schematic.load("planet.litematic")
# reg = list(schem.regions.values())[0]

# x=0
# y=0
# z=0

# block1 = region.getblock(0, 0, 0)
# for x in range(schem.width):
#     for y in range(schem.height):
#         for z in range(schem.length):
#             print(block1)
#             print(x,y,z) 
# mc.setBlock(5, 68, 5, block.GOLD_BLOCK)
from mc_remote.minecraft import Minecraft
import param_mc_remote as param
from param_mc_remote import PLAYER_ORIGIN as PO
from litemapy import Schematic

# Minecraft 接続
mc = Minecraft.create(
    address=param.ADRS_MCR,
    port=param.PORT_MCR
)
mc.setPlayer(param.PLAYER_NAME, PO.x, PO.y, PO.z)

# litematic 読み込み
schem = Schematic.load("images/sample.litematic")
region = list(schem.regions.values())[0]

# 原点（プレイヤー位置）
base_x = PO.x
base_y = PO.y
base_z = PO.z
block1 = region.getblock(1,1,1)
print(region)
print(block1) 
# block1 = region.getblock(5, 1, 5)


               

        
