import pygame
from pygame.locals import *
import time
import sys
from Python import input_status_button as button
from Python import input_status_analog as analog

def main():
    # 設定
    pygame.init()
    sensitivity = 0.5 # スティック感度設定
    accent_color = (30,227,207,1) # ON時の色
    text_top = 350 # ボタンインジケーターの1番上
    text_start1 = 20 # タンインジケーター1列目左端
    text_start2 = 170 # ボタンインジケーター2列目左端
    text_start3 = 320 # ボタンインジケーター3列目左端
    bgcolor = (242,244,246,1)

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

    # 画面の生成
    screen = pygame.display.set_mode((1000, 500))
    pygame.display.set_caption(joystick.get_name() + " " +str(joystick.get_numbuttons()) +" Buttons, " + str(joystick.get_numaxes()) +" Sticks")
    bg = pygame.image.load("img/procon.png").convert_alpha()
    rect_bg = bg.get_rect()

    while True:
        screen.fill(bgcolor)
        screen.blit(bg, rect_bg)
        pygame.draw.ellipse(screen, bgcolor, (500, 125, 250, 250))
        pygame.draw.ellipse(screen, bgcolor, (750, 125, 250, 250))
        pygame.draw.ellipse(screen, (0, 0, 0), (500, 125, 250, 250), 5)
        pygame.draw.ellipse(screen, (0, 0, 0), (750, 125, 250, 250), 5)
        button.Button_status_reset(screen, text_start1, text_start2, text_start3, text_top)
        analog.Analog_status_reset(screen)
        # イベントの取得
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                sys.exit()

            # ジョイスティックのボタンの入力

            elif e.type == pygame.JOYAXISMOTION:
                        analog.Analog_status_show(pygame, joystick, sensitivity, screen, bgcolor)
            elif e.type == pygame.locals.JOYBUTTONDOWN:
                button.button_status_show_on(joystick, screen, accent_color, text_start1, text_start2, text_start3, text_top)
                pygame.display.update()
            elif e.type == pygame.locals.JOYBUTTONUP:
                pygame.display.update()
        

if __name__=="__main__":
    main()
