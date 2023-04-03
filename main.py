import pygame
from pygame.locals import *
import time
import sys
from Python import input_status_button as button

def main():
    # 設定
    pygame.init()
    sensitivity = 0.5 # ジョイスティック感度設定
    font1 =pygame.font.SysFont("arial", 20) # フォント設定
    accent_color = (30,227,207,1)
    font_color =(0,0,0)
    text_top = 350
    text_start1 = 20
    text_start2 = 170
    text_start3 = 320

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
    pygame.display.set_caption('Nintendo Switch Pro Controller')
    bg = pygame.image.load("img/procon.png").convert_alpha()
    rect_bg = bg.get_rect()

    while True:
        screen.fill((242,244,246,1))
        screen.blit(bg, rect_bg)
        pygame.draw.ellipse(screen, (0, 0, 0), (500, 125, 250, 250), 5)
        pygame.draw.ellipse(screen, (0, 0, 0), (750, 125, 250, 250), 5)
        button.Button_status(screen, text_start1, text_start2, text_start3, text_top)
        # イベントの取得
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                sys.exit()

            # ジョイスティックのボタンの入力

            elif e.type == pygame.JOYAXISMOTION:
                        if abs((joystick.get_axis(0))) >= sensitivity or abs((joystick.get_axis(1))) >= sensitivity:
                            # print("("+str(joystick.get_axis(0))+","+ str(joystick.get_axis(1))+")")
                            pygame.draw.ellipse(screen, (0,100,0), (625 + joystick.get_axis(0) * 125, 250 + joystick.get_axis(1) * 125, 50, 50))
                            pygame.display.update()
                        elif abs((joystick.get_axis(2))) >= sensitivity or abs((joystick.get_axis(3))) >= sensitivity:
                            # print("("+str(joystick.get_axis(2))+","+ str(joystick.get_axis(3))+")")
                            pygame.draw.ellipse(screen, (0,100,0), (875, 250, 50, 50))
                            pygame.display.update()
            elif e.type == pygame.locals.JOYBUTTONDOWN:
                button.button_status_show_on(joystick, screen, accent_color, text_start1, text_start2, text_start3, text_top)
                pygame.display.update()
            elif e.type == pygame.locals.JOYBUTTONUP:
                pygame.display.update()
        

if __name__=="__main__":
    main()
