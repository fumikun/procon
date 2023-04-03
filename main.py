import pygame
from pygame.locals import *
import time

# ジョイスティック感度設定
joyL_left = 0.5
joyL_right= -0.5
joyL_up = 0.5
joyL_down =-0.5

# ジョイスティックの初期化
pygame.joystick.init()
try:
   # ジョイスティックインスタンスの生成
   joystick = pygame.joystick.Joystick(0)
   joystick.init()
   print('ジョイスティックの名前:', joystick.get_name())
   print('ボタン数 :', joystick.get_numbuttons())
except pygame.error:
   print('ジョイスティックが接続されていません')

# pygameの初期化
pygame.init()

# 画面の生成
screen = pygame.display.set_mode((320, 320))
pygame.display.set_caption('Nintendo Switch Pro Controller')


# ループ
active = True
while active:
   screen.fill((242,244,246,1))
   pygame.display.update()
   # イベントの取得
   for e in pygame.event.get():
       # 終了ボタン
       if e.type == QUIT:
           active = False

       # ジョイスティックのボタンの入力
       elif e.type == pygame.JOYAXISMOTION:
                if abs((joystick.get_axis(0))) >= 0.5 or abs((joystick.get_axis(1))) >= 0.5:
                    print("左スティック座標")
                    print("("+str(joystick.get_axis(0))+","+ str(joystick.get_axis(1))+")")
                    time.sleep(0.1)
                elif abs((joystick.get_axis(2))) >= 0.5 or abs((joystick.get_axis(3))) >= 0.5:
                    print("右スティック座標")
                    print("("+str(joystick.get_axis(2))+","+ str(joystick.get_axis(3))+")")
                    time.sleep(0.1)
       elif e.type == pygame.locals.JOYBUTTONDOWN:
           print('ボタン'+str(e.button)+'を押した')
       elif e.type == pygame.locals.JOYBUTTONUP:
           print('ボタン'+str(e.button)+'を離した')