# demo for 7-segment simulation
# using the class 'Seven_seg' in seven_seg_pg.py
# まだ あ～おまでしか作っていない
import sys
from datetime import datetime
import pygame
import pygame.freetype
# import time
from lcd_font_pg_seven_seg import LCD_font
from mc_remote.minecraft import Minecraft
import param_mc_remote as param
from param_mc_remote import PLAYER_ORIGIN as po
from param_mc_remote import block
from param_mc_remote import particle
from param_mc_remote import entity
import time
with open("fonts/font.txt", encoding="utf-8") as f:
        LCD_font_styles = f.read().split('\n')
disp_msg = "Hello World Let's play Minecraft"
i = 0
DARK_GRAY = (40, 40, 40)
GRAY = (80, 80, 80)
RED = (255, 0, 0)
GREEN = (10, 250, 10)
CYAN = (120, 120, 250)
YELLOW = (250, 250, 20)
WHITE = (250, 250, 250)
pygame.init()
clock = pygame.time.Clock()
FPS=1
BLOCKOFF=block.AIR
mc = Minecraft.create(address=param.ADRS_MCR, port=param.PORT_MCR)
result = mc.setPlayer(param.PLAYER_NAME, po.x, po.y, po.z)
if ("Error" in result):
    sys.exit(result)
else:
    print(result)
lcd1 = LCD_font(mc)


Z=45
Y=80
X=30
Yorizin=Y
Zorizin=Z
Xorizin=X
BLOCKON=block.CHERRY_PLANKS
count=0
count_2=len(disp_msg)
count_3=0
count_4=1    
for i in range (len(disp_msg)-8):
    count_3+=1
    for i in range (count_2):
            count+=1
            for i in range(count):
                msg=(ord(disp_msg[i]))
            code = msg
            print(ord(disp_msg[i]))
            Z=Zorizin
            X=Xorizin
            Y=Yorizin
            for y in range(7):
                Y-=1
                Z=Zorizin
                for x in range(5):
                    Z-=1
                    if LCD_font_styles[int(code*7+y)][x] == "1":
                        BLOCK = BLOCKON
                        mc.setBlock(X, Y,Z,BLOCK)
                    else :
                        BLOCK =BLOCKOFF
                        mc.setBlock(X, Y,Z,BLOCK)
               

                # 桁の原点
                # ドットの原点座標
                
                # ドットを描く
            Zorizin-=9
    Z=45
    Zorizin=Z
    time.sleep(0.3)
    count_2-=1
    count=0
    count+=count_3
count_2=len(disp_msg)
neo_count=10
for i in range (10):
        count+=1
        for i in range(count_2-neo_count):
            new_msg=(ord(disp_msg[i]))
        code += new_msg
        neo_count-=1
print(ord(disp_msg[i]))
    
    
                


        

# infinit loop bottom ----



