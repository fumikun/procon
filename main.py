import pygame
from pygame.locals import *
import time
from Python import main_pyqt

def main():
    # 設定
    pygame.init()
    sensitivity = 0.5 # ジョイスティック感度設定
    font1 =pygame.font.SysFont("arial", 40) # フォント設定 

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
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption('Nintendo Switch Pro Controller')
    bg = pygame.image.load("img/procon.png").convert_alpha()
    rect_bg = bg.get_rect()
    # A
    bAon = font1.render("Button A ON", True, (0,0,0))
    bAoff = font1.render("Button A OFF", True, (0,0,0))
    # B
    bBon = font1.render("Button B ON", True, (0,0,0))
    bBoff = font1.render("Button B OFF", True, (0,0,0))
    # X
    bXon = font1.render("Button X ON", True, (0,0,0))
    bXoff = font1.render("Button X OFF", True, (0,0,0))
    # Y
    bYon = font1.render("Button Y ON", True, (0,0,0))
    bYoff = font1.render("Button Y OFF", True, (0,0,0))
    # -
    bMINUSon = font1.render("Button - ON", True, (0,0,0))
    bMINUSoff = font1.render("Button - OFF", True, (0,0,0))
    # home
    bHOMEon = font1.render("Button HOME ON", True, (0,0,0))
    bHOMEoff = font1.render("Button HOME OFF", True, (0,0,0))
    # +
    bPLUSBon = font1.render("Button + ON", True, (0,0,0))
    bPLUSoff = font1.render("Button + OFF", True, (0,0,0))
    # L JOY
    bL_JOYon = font1.render("Button L JOY ON", True, (0,0,0))
    bL_JOYoff = font1.render("Button L JOY OFF", True, (0,0,0))
    # R JOY
    bR_JOYon = font1.render("Button R JOY ON", True, (0,0,0))
    bR_JOYoff = font1.render("Button R JOY OFF", True, (0,0,0))
    # L
    bLon = font1.render("Button L ON", True, (0,0,0))
    bLoff = font1.render("Button R OFF", True, (0,0,0))
    # R
    bRon = font1.render("Button R ON", True, (0,0,0))
    bRoff = font1.render("Button R OFF", True, (0,0,0))
    # UP
    bUPon = font1.render("Button UP ON", True, (0,0,0))
    bUPOff = font1.render("Button UP OFF", True, (0,0,0))
    # DOWN
    bDOWNon = font1.render("Button DOWN ON", True, (0,0,0))
    bDOWNoff = font1.render("Button DOWN OFF", True, (0,0,0))
    # LEFT
    bLEFTon = font1.render("Button LEFT ON", True, (0,0,0))
    bLEFToff = font1.render("Button LEFT OFF", True, (0,0,0))
    # RIGHT
    bRIGHTon = font1.render("Button RIGHT ON", True, (0,0,0))
    bRIGHToff = font1.render("Button RIGHT OFF", True, (0,0,0))
    # SHOT
    bSHOTon = font1.render("Button SHOT ON", True, (0,0,0))
    bSHOToff = font1.render("Button SHOT OFF", True, (0,0,0))




    # ループ
    active = True
    while True:
        screen.fill((242,244,246,1))
        screen.blit(bg, rect_bg)
        # pygame.draw.rect(screen, (255,0,0), (20,350,200,40))
        
        
        # イベントの取得
        for e in pygame.event.get():
            # 終了ボタン
            if e.type == QUIT:
                active = False

            # ジョイスティックのボタンの入力
            elif e.type == pygame.JOYAXISMOTION:
                        if abs((joystick.get_axis(0))) >= sensitivity or abs((joystick.get_axis(1))) >= sensitivity:
                            print("左スティック座標")
                            print("("+str(joystick.get_axis(0))+","+ str(joystick.get_axis(1))+")")
                            time.sleep(0.1)
                        elif abs((joystick.get_axis(2))) >= sensitivity or abs((joystick.get_axis(3))) >= sensitivity:
                            print("右スティック座標")
                            print("("+str(joystick.get_axis(2))+","+ str(joystick.get_axis(3))+")")
                            time.sleep(0.1)
            elif e.type == pygame.locals.JOYBUTTONDOWN:
                    #  pygame.draw.rect(screen, (255,0,0), (20,350,200,40))
                    screen.blit(bAon, (20, 350))
                    pygame.display.update()
            elif e.type == pygame.locals.JOYBUTTONUP:
                    #  pygame.draw.rect(screen, (255,0,0), (20,350,200,40))
                    screen.blit(bAoff, (20, 350))
                    pygame.display.update()
        

if __name__=="__main__":
    main()
