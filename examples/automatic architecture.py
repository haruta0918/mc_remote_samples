from mc_remote.minecraft import Minecraft
import param_mc_remote as param
from param_mc_remote import PLAYER_ORIGIN as PO
from param_mc_remote import block
from litemapy import Schematic, Region, BlockState
file_path = "C:\\Users\\harut\\AppData\\Roaming\\ModrinthApp\\profiles\\EarthMC (1)\\schematics\ファンタジー建築１.litematic"
schem = Schematic.load(file_path)
print(f"サイズ: 幅={schem.width}, 高さ={schem.height}, 奥行き={schem.length}")
# Create the block state we are going to use
block = BlockState("minecraft:light_blue_concrete")
reg = Region(0, 0, 0, 21, 21, 21)
# Build the planet
for x, y, z in reg.block_positions():
    if round(((x-10)**2 + (y-10)**2 + (z-10)**2)**.5) <= 10:
        reg[x, y, z] = block

# Save the schematic
schem.save("planet.litematic")
# Load the schematic and get its first region
schem = Schematic.load("planet.litematic")
reg = list(schem.regions.values())[0]

# Print out the basic shape
for x in reg.xrange():
    for z in reg.zrange():
        b = reg[x, 10, z]
        print(b.id)

        
