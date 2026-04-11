import sys
import pygame
from pygame.locals import Rect
from LCD_font_senpuuki import LCD_font_styles_se
from LCD_font_senpuuki import LCD_font_se
from pygame.locals import *
from mc_remote.minecraft import Minecraft
import param_mc_remote as param
from param_mc_remote import PLAYER_ORIGIN as PO
from param_mc_remote import block
from time import sleep
mc = Minecraft.create(address=param.ADRS_MCR, port=param.PORT_MCR)
mc.setPlayer(param.PLAYER_NAME, PO.x, PO.y, PO.z)
pygame.init()

WHITE = (250, 250, 250)
BLUE = (100, 100, 255)
BLACK = (0, 0, 0)
ORIZINARU = (0, 230, 0)

screen = pygame.display.set_mode([1200, 600])
pygame.display.set_caption("senpuuki")
mouse_x, mouse_y = pygame.mouse.get_pos()
screen.fill((100, 100, 255))
x1 = 0
y1 = 0
z1 = 0
scale = 1
x2 = 0
y2 = 0
z2 = 0
scale2 = 0
mazix = 0
maziy = 0
maziz = 0
x = mazix
y = maziy
z = maziz
sakusei = 0
maru = 0
osita = 0
air = 0
priset1x = 0
priset1y = 0
priset1z = 0
priset1maru = 0
priset2x = 0
priset2y = 0
priset2z = 0
priset2maru = 0
priset3x = 0
priset3y = 0
priset3z = 0
priset3maru = 0
purasux = 1
purasuy = 1
purasuz = 1
pygame.draw.polygon(screen, BLACK, [(120, 30), (30, 70), (120, 110)])
pygame.draw.polygon(screen, BLACK, [(480, 30), (570, 70), (480, 110)])
pygame.draw.polygon(screen, BLACK, [(120, 140), (30, 180), (120, 220)])
pygame.draw.polygon(screen, BLACK, [(480, 140), (570, 180), (480, 220)])
pygame.draw.polygon(screen, BLACK, [(120, 250), (30, 290), (120, 330)])
pygame.draw.polygon(screen, BLACK, [(480, 250), (570, 290), (480, 330)])
pygame.draw.polygon(screen, BLACK, [(120, 360), (30, 400), (120, 440)])
pygame.draw.polygon(screen, BLACK, [(480, 360), (570, 400), (480, 440)])
pygame.draw.rect(screen, BLACK, Rect(650, 335, 450, 100))
pygame.draw.rect(screen, BLACK, Rect(650, 195, 450, 100))
pygame.draw.rect(screen, BLACK, Rect(650, 55, 450, 100))
pygame.draw.rect(screen, BLACK, Rect(700, 460, 400, 100))
xlcd = LCD_font_se(screen)
xlcd.init_col(BLOCK_SIZE=13, BLOCK_INTV=13, COLOR_ON=BLACK, COLOR_OFF=BLUE)
xlcd.init_row(X_ORG=12, Y_ORG=1, COL_INTV=6)
ylcd = LCD_font_se(screen)
ylcd.init_col(BLOCK_SIZE=13, BLOCK_INTV=13, COLOR_ON=BLACK, COLOR_OFF=BLUE)
ylcd.init_row(X_ORG=12, Y_ORG=9.5, COL_INTV=6)
zlcd = LCD_font_se(screen)
zlcd.init_col(BLOCK_SIZE=13, BLOCK_INTV=13, COLOR_ON=BLACK, COLOR_OFF=BLUE)
zlcd.init_row(X_ORG=12, Y_ORG=18, COL_INTV=6)
scalelcd = LCD_font_se(screen)
scalelcd.init_col(BLOCK_SIZE=8, BLOCK_INTV=8, COLOR_ON=BLACK, COLOR_OFF=BLUE)
scalelcd.init_row(X_ORG=18, Y_ORG=46, COL_INTV=5.5)
makelcd = LCD_font_se(screen)
makelcd.init_col(BLOCK_SIZE=10, BLOCK_INTV=10, COLOR_ON=WHITE, COLOR_OFF=BLACK)
makelcd.init_row(X_ORG=77, Y_ORG=47, COL_INTV=7)
suutixlcd = LCD_font_se(screen)
suutixlcd.init_col(BLOCK_SIZE=9, BLOCK_INTV=9, COLOR_ON=BLACK, COLOR_OFF=BLUE)
suutixlcd.init_row(X_ORG=41.5, Y_ORG=4.5, COL_INTV=6)
suutiylcd = LCD_font_se(screen)
suutiylcd.init_col(BLOCK_SIZE=9, BLOCK_INTV=9, COLOR_ON=BLACK, COLOR_OFF=BLUE)
suutiylcd.init_row(X_ORG=41.5, Y_ORG=16.5, COL_INTV=6)
suutizlcd = LCD_font_se(screen)
suutizlcd.init_col(BLOCK_SIZE=9, BLOCK_INTV=9, COLOR_ON=BLACK, COLOR_OFF=BLUE)
suutizlcd.init_row(X_ORG=41.5, Y_ORG=28.5, COL_INTV=6)
suutiscalelcd = LCD_font_se(screen)
suutiscalelcd.init_col(BLOCK_SIZE=9, BLOCK_INTV=9, COLOR_ON=BLACK, COLOR_OFF=BLUE)
suutiscalelcd.init_row(X_ORG=41.5, Y_ORG=40.5, COL_INTV=6)
purasuxlcd = LCD_font_se(screen)
purasuxlcd.init_col(BLOCK_SIZE=9, BLOCK_INTV=9, COLOR_ON=BLACK, COLOR_OFF=BLUE)
purasuxlcd.init_row(X_ORG=35.5, Y_ORG=4.5, COL_INTV=6)
purasuylcd = LCD_font_se(screen)
purasuylcd.init_col(BLOCK_SIZE=9, BLOCK_INTV=9, COLOR_ON=BLACK, COLOR_OFF=BLUE)
purasuylcd.init_row(X_ORG=35.5, Y_ORG=16.5, COL_INTV=6)
purasuzlcd = LCD_font_se(screen)
purasuzlcd.init_col(BLOCK_SIZE=9, BLOCK_INTV=9, COLOR_ON=BLACK, COLOR_OFF=BLUE)
purasuzlcd.init_row(X_ORG=35.5, Y_ORG=28.5, COL_INTV=6)
airlcd = LCD_font_se(screen)
airlcd.init_col(BLOCK_SIZE=10, BLOCK_INTV=10, COLOR_ON=BLACK, COLOR_OFF=BLUE)
airlcd.init_row(X_ORG=15, Y_ORG=48, COL_INTV=6)
batsumarulcd = LCD_font_se(screen)
batsumarulcd.init_col(BLOCK_SIZE=14, BLOCK_INTV=14, COLOR_ON=BLACK, COLOR_OFF=BLUE)
batsumarulcd.init_row(X_ORG=27, Y_ORG=33.5, COL_INTV=6)
priset1lcd = LCD_font_se(screen)
priset1lcd.init_col(BLOCK_SIZE=14, BLOCK_INTV=14, COLOR_ON=WHITE, COLOR_OFF=BLACK)
priset1lcd.init_row(X_ORG=80, Y_ORG=4, COL_INTV=6)
priset2lcd = LCD_font_se(screen)
priset2lcd.init_col(BLOCK_SIZE=14, BLOCK_INTV=14, COLOR_ON=WHITE, COLOR_OFF=BLACK)
priset2lcd.init_row(X_ORG=80, Y_ORG=14, COL_INTV=6)
priset3lcd = LCD_font_se(screen)
priset3lcd.init_col(BLOCK_SIZE=14, BLOCK_INTV=14, COLOR_ON=WHITE, COLOR_OFF=BLACK)
priset3lcd.init_row(X_ORG=80, Y_ORG=24, COL_INTV=6)
signup1lcd = LCD_font_se(screen)
signup1lcd.init_col(BLOCK_SIZE=10, BLOCK_INTV=10, COLOR_ON=WHITE, COLOR_OFF=BLACK)
signup1lcd.init_row(X_ORG=67, Y_ORG=7, COL_INTV=6)
signup2lcd = LCD_font_se(screen)
signup2lcd.init_col(BLOCK_SIZE=10, BLOCK_INTV=10, COLOR_ON=WHITE, COLOR_OFF=BLACK)
signup2lcd.init_row(X_ORG=67, Y_ORG=21, COL_INTV=6)
signup3lcd = LCD_font_se(screen)
signup3lcd.init_col(BLOCK_SIZE=10, BLOCK_INTV=10, COLOR_ON=WHITE, COLOR_OFF=BLACK)
signup3lcd.init_row(X_ORG=67, Y_ORG=35, COL_INTV=6)
xlcd.update_col(col=0, code=63)
ylcd.update_col(col=0, code=64)
zlcd.update_col(col=0, code=65)
scalelcd.update_col(col=0, code=58)
scalelcd.update_col(col=1, code=42)
scalelcd.update_col(col=2, code=40)
scalelcd.update_col(col=3, code=51)
scalelcd.update_col(col=4, code=44)
makelcd.update_col(col=0, code=52)
makelcd.update_col(col=1, code=40)
makelcd.update_col(col=2, code=50)
makelcd.update_col(col=3, code=44)
suutixlcd.update_col(col=1, code=x1/1%10)
suutixlcd.update_col(col=0, code=x1/10%10)
suutiylcd.update_col(col=1, code=y1/1%10)
suutiylcd.update_col(col=0, code=y1/10%10)
suutizlcd.update_col(col=1, code=z1/1%10)
suutizlcd.update_col(col=0, code=z1/10%10)
suutiscalelcd.update_col(col=1, code=scale/1%10)
purasuxlcd.update_col(col=0, code=69)
purasuylcd.update_col(col=0, code=69)
purasuzlcd.update_col(col=0, code=69)
airlcd.update_col(col=0, code=40)
airlcd.update_col(col=1, code=48)
airlcd.update_col(col=2, code=57)
batsumarulcd.update_col(col=0, code=71)
airlcd.update_col(col=1, code=48)
airlcd.update_col(col=2, code=57)
priset1lcd.update_col(col=0, code=1)
priset2lcd.update_col(col=0, code=2)
priset3lcd.update_col(col=0, code=3)
signup1lcd.update_col(col=0, code=58)
signup1lcd.update_col(col=1, code=48)
signup1lcd.update_col(col=2, code=46)
signup1lcd.update_col(col=3, code=53)
signup1lcd.update_col(col=5, code=60)
signup1lcd.update_col(col=6, code=55)
signup2lcd.update_col(col=0, code=58)
signup2lcd.update_col(col=1, code=48)
signup2lcd.update_col(col=2, code=46)
signup2lcd.update_col(col=3, code=53)
signup2lcd.update_col(col=5, code=60)
signup2lcd.update_col(col=6, code=55)
signup3lcd.update_col(col=0, code=58)
signup3lcd.update_col(col=1, code=48)
signup3lcd.update_col(col=2, code=46)
signup3lcd.update_col(col=3, code=53)
signup3lcd.update_col(col=5, code=60)
signup3lcd.update_col(col=6, code=55)
#12=!,13=?,14=A,15=B,16=C,17=D,18=E,19=F,20=G,21=H,22=I,23=J,24=K
#25=L,26=M,27=N,28=O,29=P,30=Q,31=R,32=S,33=T,34=U,35=V,36=W,37=X
#38=Y,39=Z,40=a,41=b,42=c,43=d,44=e,45=f,46=g,47=h,48=i,49=j,50=k
#51=l,52=m,53=n,54=o,55=p,56=q,57=r,58=s,59=t,60=u,61=v,62=w,63=x
#64=y,65=z,66=',67=.,68=, 69=+, 70=-, 71=×, 72=〇
running = True
while running:
    mouse_x, mouse_y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if not running:
            break
        if event.type == pygame.KEYDOWN:
            if pygame.K_SPACE:
                print(f"a: ({mouse_x}, {mouse_y}, {x1}, {y1}, {z1}, {scale}, {priset1x}, {priset1y}, {priset1z}, {priset2x}, {priset2y}, {priset2z}, {priset3x}, {priset3y}, {priset3z}, {maru}, {priset1maru}, {priset2maru}, {priset3maru}, {priset1purasux}, {priset1purasuy}, {priset1purasuz}, {purasux}, {purasuy}, {purasuz})")
                

    if event.type == pygame.MOUSEBUTTONDOWN:
        if mouse_x > 480 and mouse_x < 565 and mouse_y > 30 and mouse_y < 110:
            if x2 == 0:
                if mazix < 50:
                    if mazix < 0:
                        x1 = x1 - 1
                    if mazix > -1:
                        x1 = x1 + 1
                    mazix = mazix + 1
                    x2 = 1
                    suutixlcd.update_col(col=1, code=x1/1%10)
                    suutixlcd.update_col(col=0, code=x1/10%10)
        if mouse_x > 35 and mouse_x < 120 and mouse_y > 30 and mouse_y < 110:
            if x2 == 0:
                if mazix > -50:
                    if mazix < 1:
                        x1 = x1 + 1
                    else:
                        x1 = x1 - 1
                    mazix = mazix - 1
                    x2 = 1
                    suutixlcd.update_col(col=1, code=x1/1%10)
                    suutixlcd.update_col(col=0, code=x1/10%10)
        if mouse_x > 480 and mouse_x < 565 and mouse_y > 140 and mouse_y < 220:
            if y2 == 0:
                if maziy < 50:
                    if maziy < 0:
                        y1 = y1 - 1
                    if maziy > -1:
                        y1 = y1 + 1
                    maziy = maziy + 1
                    y2 = 1
                    suutiylcd.update_col(col=1, code=y1/1%10)
                    suutiylcd.update_col(col=0, code=y1/10%10)
        if mouse_x > 35 and mouse_x < 120 and mouse_y > 140 and mouse_y < 220:
            if y2 == 0:
                if maziy > -50:
                    if maziy < 1:
                        y1 = y1 + 1
                    else:
                        y1 = y1 - 1
                    maziy = maziy - 1
                    y2 = 1
                    suutiylcd.update_col(col=1, code=y1/1%10)
                    suutiylcd.update_col(col=0, code=y1/10%10)
        if mouse_x > 480 and mouse_x < 565 and mouse_y > 250 and mouse_y < 330:
            if z2 == 0:
                if maziz < 50:
                    if maziz < 0:
                        z1 = z1 - 1
                    if maziz > -1:
                        z1 = z1 + 1
                    maziz = maziz + 1
                    z2 = 1
                    suutizlcd.update_col(col=1, code=z1/1%10)
                    suutizlcd.update_col(col=0, code=z1/10%10)
        if mouse_x > 35 and mouse_x < 120 and mouse_y > 250 and mouse_y < 330:
            if z2 == 0:
                if maziz > -50:
                    if maziz < 1:
                        z1 = z1 + 1
                    else:
                        z1 = z1 - 1
                    maziz = maziz - 1
                    z2 = 1
                    suutizlcd.update_col(col=1, code=z1/1%10)
                    suutizlcd.update_col(col=0, code=z1/10%10)
        if mouse_x > 480 and mouse_x < 565 and mouse_y > 360 and mouse_y < 440:
            if scale2 == 0:
                if scale < 3:
                    scale = scale + 1
                    scale2 = 1
                    suutiscalelcd.update_col(col=1, code=scale/1%10)
        if mouse_x > 35 and mouse_x < 120 and mouse_y > 360 and mouse_y < 440:
            if scale2 == 0:
                if scale > 1:
                    scale = scale - 1
                    scale2 = 1
                    suutiscalelcd.update_col(col=1, code=scale/1%10)
        if mouse_x > 365 and mouse_x < 460 and mouse_y > 470 and mouse_y < 580:
            if osita == 0:
                if maru == 0:
                    maru = 1
                    osita = 1
                    batsumarulcd.update_col(col=0, code=72)
                    air = 1
                else:
                    maru = 0
                    osita = 1
                    batsumarulcd.update_col(col=0, code=71)
                    air = 0
        if mouse_x > 650 and mouse_x < 1100 and mouse_y > 55 and mouse_y < 155:
            priset1x = x1
            priset1y = y1
            priset1z = z1
            priset1maru = maru
            priset1purasux = purasux
            priset1purasuy = purasuy
            priset1purasuz = purasuz

        if mouse_x > 650 and mouse_x < 1100 and mouse_y > 195 and mouse_y < 295:
            priset2x = x1
            priset2y = y1
            priset2z = z1
            priset2maru = maru
            priset2purasux = purasux
            priset2purasuy = purasuy
            priset2purasuz = purasuz

        if mouse_x > 650 and mouse_x < 1100 and mouse_y > 335 and mouse_y < 435:
            priset3x = x1
            priset3y = y1
            priset3z = z1
            priset3maru = maru
            priset3purasux = purasux
            priset3purasuy = purasuy
            priset3purasuz = purasuz

        if mouse_x > 1120 and mouse_x < 1190 and mouse_y > 55 and mouse_y < 155:
            x1 = priset1x
            y1 = priset1y
            z1 = priset1z
            if priset1purasux == 0:
                mazix = priset1x - priset1x * 2
            else:
                mazix = priset1x
            if priset1purasuy == 0:
                maziy = priset1y - priset1y * 2
            else:
                maziy = priset1y
            if priset1purasuz == 0:
                maziz = priset1z - priset1z * 2
            else:
                maziz = priset1z
            maru = priset1maru
            suutixlcd.update_col(col=1, code=x1/1%10)
            suutixlcd.update_col(col=0, code=x1/10%10)
            suutiylcd.update_col(col=1, code=y1/1%10)
            suutiylcd.update_col(col=0, code=y1/10%10)
            suutizlcd.update_col(col=1, code=z1/1%10)
            suutizlcd.update_col(col=0, code=z1/10%10)
            suutiscalelcd.update_col(col=1, code=scale/1%10)
            if maru == 0:
                batsumarulcd.update_col(col=0, code=71)
                air = 0
            if maru == 1:
                batsumarulcd.update_col(col=0, code=72)
                air = 1

        if mouse_x > 1120 and mouse_x < 1190 and mouse_y > 195 and mouse_y < 295:
            x1 = priset2x
            y1 = priset2y
            z1 = priset2z
            if priset2purasux == 0:
                mazix = priset2x - priset2x * 2
            else:
                mazix = priset2x
            if priset2purasuy == 0:
                maziy = priset2y - priset2y * 2
            else:
                maziy = priset2y
            if priset2purasuz == 0:
                maziz = priset2z - priset2z * 2
            else:
                maziz = priset2z
            maru = priset2maru
            suutixlcd.update_col(col=1, code=x1/1%10)
            suutixlcd.update_col(col=0, code=x1/10%10)
            suutiylcd.update_col(col=1, code=y1/1%10)
            suutiylcd.update_col(col=0, code=y1/10%10)
            suutizlcd.update_col(col=1, code=z1/1%10)
            suutizlcd.update_col(col=0, code=z1/10%10)
            suutiscalelcd.update_col(col=1, code=scale/1%10)
            if maru == 0:
                batsumarulcd.update_col(col=0, code=71)
                air = 0
            if maru == 1:
                batsumarulcd.update_col(col=0, code=72)
                air = 1

        if mouse_x > 1120 and mouse_x < 1190 and mouse_y > 335 and mouse_y < 435:
            x1 = priset3x
            y1 = priset3y
            z1 = priset3z
            if priset3purasux == 0:
                mazix = priset3x - priset3x * 2
            else:
                mazix = priset3x
            if priset3purasuy == 0:
                maziy = priset3y - priset3y * 2
            else:
                maziy = priset3y
            if priset3purasuz == 0:
                maziz = priset3z - priset3z * 2
            else:
                maziz = priset3z
            maru = priset3maru
            suutixlcd.update_col(col=1, code=x1/1%10)
            suutixlcd.update_col(col=0, code=x1/10%10)
            suutiylcd.update_col(col=1, code=y1/1%10)
            suutiylcd.update_col(col=0, code=y1/10%10)
            suutizlcd.update_col(col=1, code=z1/1%10)
            suutizlcd.update_col(col=0, code=z1/10%10)
            suutiscalelcd.update_col(col=1, code=scale/1%10)
            if maru == 0:
                batsumarulcd.update_col(col=0, code=71)
                air = 0
            if maru == 1:
                batsumarulcd.update_col(col=0, code=72)
                air = 1

        if mouse_x > 700 and mouse_x < 1100 and mouse_y > 460 and mouse_y < 560:
            if scale == 1:
                if sakusei == 0:
                    x = mazix
                    y = maziy
                    z = maziz

                    ## 扇風機 scale 1
                    if air == 1:
                        x += 2
                        for _i in range(3):
                            for _i in range(7):
                                for _i in range(9):
                                    mc.setBlock(x, y, z, block.AIR)
                                    y += 1
                                y -= 9
                                x -= 1
                            x += 7
                            z += 1
                        z -= 3
                        x -= 2
                    
                    for _i in range(3):
                        for _i in range(3):
                            mc.setBlock(x, y, z, block.WHITE_CONCRETE)
                            z += 1
                        x -= 1
                        z -= 3
                    x += 2
                    z += 1
                    for _i in range(3):
                        mc.setBlock(x, y, z, block.WHITE_CONCRETE)
                        y += 1
                    y -= 1
                    x += 1
                    for _i in range(3):
                        mc.setBlock(x, y, z, block.WHITE_CONCRETE)
                        x -= 1
                    y += 1
                    mc.setBlock(x, y, z, block.WHITE_CONCRETE)
                    x -= 1
                    y += 1
                    for _i in range(3):
                        mc.setBlock(x, y, z, block.WHITE_CONCRETE)
                        y += 1
                    x += 1
                    mc.setBlock(x, y, z, block.WHITE_CONCRETE)
                    x += 1
                    y += 1
                    for _i in range(3):
                        mc.setBlock(x, y, z, block.WHITE_CONCRETE)
                        x += 1
                    y -= 1
                    mc.setBlock(x, y, z, block.WHITE_CONCRETE)
                    y -= 1
                    x += 1
                    for _i in range(3):
                        mc.setBlock(x, y, z, block.WHITE_CONCRETE)
                        y -= 1
                    x -= 1
                    mc.setBlock(x, y, z, block.WHITE_CONCRETE)
                    z += 1
                    x -= 2
                    for _i in range(5):
                        mc.setBlock(x, y, z, block.WHITE_CONCRETE)
                        y += 1
                    x += 2
                    y -= 3
                    for _i in range(5):
                        mc.setBlock(x, y, z, block.WHITE_CONCRETE)
                        x -= 1
                    x += 2
                    y += 1
                    for _i in range(3):
                        for _i in range(3):
                            mc.setBlock(x, y, z, block.WHITE_CONCRETE)
                            x += 1
                        y -= 1
                        x -= 3
                    z -= 1
                    x += 1
                    y += 1
                    for _i in range(3):
                        mc.setBlock(x, y, z, block.LIGHT_BLUE_CONCRETE)
                        y += 1
                    y -= 2
                    x -= 1
                    for _i in range(3):
                        mc.setBlock(x, y, z, block.LIGHT_BLUE_CONCRETE)
                        x += 1
                    sakusei = 1    

            if scale == 2:
                if sakusei == 0:
                    x = mazix
                    y = maziy
                    z = maziz

                    ## 扇風機 scale 2
                    if air == 1:
                        x += 2
                        for _i in range(5):
                            for _i in range(9):
                                for _i in range(14):
                                    mc.setBlock(x, y, z, block.AIR)
                                    y += 1
                                y -= 14
                                x -= 1
                            x += 9
                            z += 1
                        z -= 5
                        x -= 2

                    for _i in range(5):
                        for _i in range(5):
                            mc.setBlock(x, y, z, block.WHITE_CONCRETE)
                            z += 1
                        x -= 1
                        z -= 5
                    y += 1
                    x += 4
                    z += 1
                    for _i in range(3):
                        for _i in range(3):
                            mc.setBlock(x, y, z, block.WHITE_CONCRETE)
                            z += 1
                        x -= 1
                        z -= 3
                    y += 1
                    x += 2
                    z += 1
                    for _i in range(4):
                        mc.setBlock(x, y, z, block.WHITE_CONCRETE)
                        y += 1
                    y -= 1
                    x -= 2
                    for _i in range(5):
                         mc.setBlock(x, y, z, block.WHITE_CONCRETE)
                         x += 1
                    y += 1
                    mc.setBlock(x, y, z, block.WHITE_CONCRETE)
                    y += 1
                    x += 1
                    for _i in range(5):
                        mc.setBlock(x, y, z, block.WHITE_CONCRETE)
                        y += 1
                    x -= 1
                    mc.setBlock(x, y, z, block.WHITE_CONCRETE)
                    x -= 1
                    y += 1
                    for _i in range(5):
                        mc.setBlock(x, y, z, block.WHITE_CONCRETE)
                        x -= 1
                    y -= 1
                    mc.setBlock(x, y, z, block.WHITE_CONCRETE)
                    y -= 1
                    x -= 1
                    for _i in range(5):
                        mc.setBlock(x, y, z, block.WHITE_CONCRETE)
                        y -= 1
                    x += 1
                    mc.setBlock(x, y, z, block.WHITE_CONCRETE)
                    y += 3
                    z += 1
                    for _i in range(7):
                        mc.setBlock(x, y, z, block.WHITE_CONCRETE)
                        x += 1
                    x -= 4
                    y += 3
                    for _i in range(7):
                        mc.setBlock(x, y, z, block.WHITE_CONCRETE)
                        y -= 1
                    x += 2
                    y += 2
                    for _i in range(5):
                        mc.setBlock(x, y, z, block.WHITE_CONCRETE)
                        x -= 1
                        y += 1
                    y -= 5
                    x += 1
                    for _i in range(5):
                        mc.setBlock(x, y, z, block.WHITE_CONCRETE)
                        x += 1
                        y += 1
                    x -= 3
                    z -= 1
                    y -= 1
                    for _i in range(5):
                        mc.setBlock(x, y, z, block.LIGHT_BLUE_CONCRETE)
                        y -= 1
                    x += 2
                    y += 3
                    for _i in range(5):
                        mc.setBlock(x, y, z, block.LIGHT_BLUE_CONCRETE)
                        x -= 1
                    sakusei = 1  

            if scale == 3:
                if sakusei == 0:
                    x = mazix
                    y = maziy
                    z = maziz

                    ## 扇風機 scale 3
                    if air == 1:
                        x += 2
                        for _i in range(7):
                            for _i in range(11):
                                for _i in range(19):
                                    mc.setBlock(x, y, z, block.AIR)
                                    y += 1
                                y -= 19
                                x -= 1
                            x += 11
                            z += 1
                        z -= 7
                        x -= 2
                    
                    for _i in range(7):
                        for _i in range(7):
                            mc.setBlock(x, y, z, block.WHITE_CONCRETE)
                            x -= 1
                        x += 7
                        z += 1
                    z -= 2
                    x -= 1
                    y += 1
                    for _i in range(5):
                        for _i in range(5):
                            mc.setBlock(x, y, z, block.WHITE_CONCRETE)
                            x -= 1
                        x += 5
                        z -= 1
                    x -= 1
                    z += 2
                    y += 1
                    for _i in range(3):
                        for _i in range(3):
                            mc.setBlock(x, y, z, block.WHITE_CONCRETE)
                            x -= 1
                        x += 3
                        z += 1
                    z -= 2
                    x -= 1
                    y += 1
                    for _i in range(5):
                        mc.setBlock(x, y, z, block.WHITE_CONCRETE)
                        y += 1
                    x += 2
                    for _i in range(5):
                        mc.setBlock(x, y, z, block.WHITE_CONCRETE)
                        x -= 1
                    y += 1
                    mc.setBlock(x, y, z, block.WHITE_CONCRETE)
                    x -= 1
                    y += 1
                    mc.setBlock(x, y, z, block.WHITE_CONCRETE)
                    x -= 1
                    y += 1
                    for _i in range(5):
                        mc.setBlock(x, y, z, block.WHITE_CONCRETE)
                        y += 1
                    x += 1
                    mc.setBlock(x, y, z, block.WHITE_CONCRETE)
                    x += 1
                    y += 1
                    mc.setBlock(x, y, z, block.WHITE_CONCRETE)
                    x += 1
                    y += 1
                    for _i in range(5):
                        mc.setBlock(x, y, z, block.WHITE_CONCRETE)
                        x += 1
                    y -= 1
                    mc.setBlock(x, y, z, block.WHITE_CONCRETE)
                    x += 1
                    y -= 1
                    mc.setBlock(x, y, z, block.WHITE_CONCRETE)
                    x += 1
                    y -= 1
                    for _i in range(5):
                        mc.setBlock(x, y, z, block.WHITE_CONCRETE)
                        y -= 1
                    x -= 1
                    mc.setBlock(x, y, z, block.WHITE_CONCRETE)
                    x -= 1
                    y -= 1
                    mc.setBlock(x, y, z, block.WHITE_CONCRETE)
                    z += 1
                    x -= 3
                    for _i in range(9):
                        mc.setBlock(x, y, z, block.WHITE_CONCRETE)
                        y += 1
                    x -= 4
                    y -= 5
                    for _i in range(9):
                        mc.setBlock(x, y, z, block.WHITE_CONCRETE)
                        x += 1
                    y += 3
                    x -= 2
                    for _i in range(7):
                        mc.setBlock(x, y, z, block.WHITE_CONCRETE)
                        x -= 1
                        y -= 1
                    y += 7
                    x += 1
                    for _i in range(7):
                        mc.setBlock(x, y, z, block.WHITE_CONCRETE)
                        x += 1
                        y -= 1
                    z -= 1
                    x -= 4
                    y += 1
                    for _i in range(7):
                        mc.setBlock(x, y, z, block.LIGHT_BLUE_CONCRETE)
                        y += 1
                    y -= 4
                    x -= 3
                    for _i in range(7):
                        mc.setBlock(x, y, z, block.LIGHT_BLUE_CONCRETE)
                        x += 1

    if event.type == pygame.MOUSEBUTTONUP:
        x2 = 0
        y2 = 0
        z2 = 0
        scale2 = 0
        sakusei = 0
        osita = 0

    if mazix > -1:
        purasuxlcd.update_col(col=0, code=69)
        purasux = 1
    else:
        purasuxlcd.update_col(col=0, code=70)
        purasux = 0
    if maziy > -1:
        purasuylcd.update_col(col=0, code=69)
        purasuy = 1
    else:
        purasuylcd.update_col(col=0, code=70)
        purasuy = 0
    if maziz > -1:
        purasuzlcd.update_col(col=0, code=69)
        purasuz = 1
    else:
        purasuzlcd.update_col(col=0, code=70)
        purasuz = 0
    
    pygame.display.flip()
pygame.quit()
print(x1,y1,z1,scale)


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
X0, Y0, Z0 = x1, y1+63,z1
sleep(2)
# Load the schematic and get its first region
schem = Schematic.load(file_name)
reg = list(schem.regions.values())[0]
size = scale 
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
                        mc.setBlock(X0+X1+X2, Y0 +Y1+Y2,Z0+Z1+Z2, b.id)
                        print(X0+X1+X2, Y0 +Y1+Y2,Z0+Z1+Z2, b.id)
                        sleep(0.01)
                        Z1 +=1  
                    Y1 +=1
                X1 +=1
        X2=0
    Y2=0                




