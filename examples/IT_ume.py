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
from litemapy import Schematic, Region, BlockState
import tkinter as tk
from tkinter import filedialog
import os

mc = Minecraft.create(address=param.ADRS_MCR, port=param.PORT_MCR)
mc.setPlayer(param.PLAYER_NAME, PO.x, PO.y, PO.z)
pygame.init()

try:
    label_font = pygame.font.Font("fonts/natumemozi.ttf", 22)
except Exception:
    label_font = pygame.font.SysFont(None, 24)

WHITE = (250, 250, 250)
BLUE = (100, 100, 255)
BLACK = (0, 0, 0)
ORIZINARU = (0, 230, 0)
GRAY = (60, 60, 60)

screen = pygame.display.set_mode([500, 600])
pygame.display.set_caption("ピラミッド")
mouse_x, mouse_y = pygame.mouse.get_pos()
screen.fill((100, 100, 255))

step = 1
step2 = 0
maru = 0
osita = 0
air = 0

pygame.draw.rect(screen, BLACK, Rect(50, 475, 400, 100))

steplcd = LCD_font_se(screen)
steplcd.init_col(BLOCK_SIZE=8, BLOCK_INTV=8, COLOR_ON=BLACK, COLOR_OFF=BLUE)
steplcd.init_row(X_ORG=18, Y_ORG=46, COL_INTV=5.5)
makelcd = LCD_font_se(screen)
makelcd.init_col(BLOCK_SIZE=10, BLOCK_INTV=10, COLOR_ON=WHITE, COLOR_OFF=BLACK)
makelcd.init_row(X_ORG=12, Y_ORG=48.5, COL_INTV=7)
suutisteplcd = LCD_font_se(screen)
suutisteplcd.init_col(BLOCK_SIZE=9, BLOCK_INTV=9, COLOR_ON=BLACK, COLOR_OFF=BLUE)
suutisteplcd.init_row(X_ORG=41.5, Y_ORG=40.5, COL_INTV=6)
airlcd = LCD_font_se(screen)
airlcd.init_col(BLOCK_SIZE=10, BLOCK_INTV=10, COLOR_ON=BLACK, COLOR_OFF=BLUE)
airlcd.init_row(X_ORG=15, Y_ORG=48, COL_INTV=6)
batsumarulcd = LCD_font_se(screen)
batsumarulcd.init_col(BLOCK_SIZE=14, BLOCK_INTV=14, COLOR_ON=BLACK, COLOR_OFF=BLUE)
batsumarulcd.init_row(X_ORG=27, Y_ORG=33.5, COL_INTV=6)

makelcd.update_col(col=0, code=52)
makelcd.update_col(col=1, code=40)
makelcd.update_col(col=2, code=50)
makelcd.update_col(col=3, code=44)
l=0
#12=!,13=?,14=A,15=B,16=C,17=D,18=E,19=F,20=G,21=H,22=I,23=J,24=K
#25=L,26=M,27=N,28=O,29=P,30=Q,31=R,32=S,33=T,34=U,35=V,36=W,37=X
#38=Y,39=Z,40=a,41=b,42=c,43=d,44=e,45=f,46=g,47=h,48=i,49=j,50=k
#51=l,52=m,53=n,54=o,55=p,56=q,57=r,58=s,59=t,60=u,61=v,62=w,63=x
#64=y,65=z,66=',67=.,68=, 69=+, 70=-, 71=×, 72=〇

# ==== ブロックの選択肢 ====
BLOCK_OPTIONS = [
    ("石レンガ",                block.STONE_BRICKS),
    ("ガラス",                  block.GLASS),
    ("シーランタン",            block.SEA_LANTERN),
    ("クォーツブロック",         block.QUARTZ_BLOCK),
    ("銅ブロック",              block.COPPER_BLOCK),
    ("鉄ブロック",              block.IRON_BLOCK),
    ("金ブロック",              block.GOLD_BLOCK),
    ("ダイヤモンドブロック",     block.DIAMOND_BLOCK),
    ("ネザライトブロック",       block.NETHERITE_BLOCK),
    ("エメラルドブロック",       block.EMERALD_BLOCK),

    
   
]

selected_block_index = 7  # 初期選択（元コードで使っていた SMOOTH_QUARTZ）

PANEL_X = 95
PANEL_Y = 40
ROW_HEIGHT = 42
ROW_WIDTH = 300

def draw_block_panel():
    # パネル部分だけ塗りつぶしてから再描画（毎回全画面を再描画しないため）
    pygame.draw.rect(screen, (100, 100, 255), Rect(PANEL_X - 10, PANEL_Y - 10, ROW_WIDTH + 20, ROW_HEIGHT * len(BLOCK_OPTIONS) + 20))
    title_surface = label_font.render("使うブロックを選んでください", True, BLACK)
    screen.blit(title_surface, (PANEL_X - 10, PANEL_Y - 35))
    for i, (label, _) in enumerate(BLOCK_OPTIONS):
        row_y = PANEL_Y + i * ROW_HEIGHT
        circle_center = (PANEL_X + 14, row_y + ROW_HEIGHT // 2 - 5)
        pygame.draw.circle(screen, BLACK, circle_center, 9, 2)  # 枠だけの丸
        if i == selected_block_index:
            pygame.draw.circle(screen, BLACK, circle_center, 5)  # 選択中は中を塗りつぶす
        text_surface = label_font.render(label, True, BLACK)
        screen.blit(text_surface, (PANEL_X + 32, row_y))

draw_block_panel()

running = True
while running:
    mouse_x, mouse_y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if not running:
            break

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print(f"a: ({mouse_x}, {mouse_y}, {step}, {maru})")
        if event.type == pygame.MOUSEBUTTONDOWN:

            # ==== ブロック選択パネルのクリック判定 ====
            if PANEL_X - 10 <= mouse_x <= PANEL_X - 10 + ROW_WIDTH + 20:
                for i in range(len(BLOCK_OPTIONS)):
                    row_y = PANEL_Y + i * ROW_HEIGHT
                    if row_y <= mouse_y <= row_y + ROW_HEIGHT:
                        selected_block_index = i
                        draw_block_panel()
                        break

            # ==== 自動建築の実行部分 ====
            if mouse_x > 50 and mouse_x < 450 and mouse_y > 475 and mouse_y < 575:
                BLOCK = BLOCK_OPTIONS[selected_block_index][1]
                X=0
                Y=63
                Z=0
                size=5
                size2=0
                for i in range(size):
                    X=size2
                    for i in range(size):
                        Z=size2
                        for i in range(size):
                            mc.setBlock(X,Y,Z, BLOCK)
                            print(X,Y,Z)
                            Z+=1
                        X+=1
                    Y+=1
                    size-=2
                    size2+=1

            # ================================================================

        if event.type == pygame.MOUSEBUTTONUP:
            step2 = 0
            osita = 0

    pygame.display.flip()
pygame.quit()