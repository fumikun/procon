import pygame
from pygame.locals import *
import time

def Button_status(screen, t1, t2, t3, tt):
    font1 =pygame.font.SysFont("arial", 20) # フォント設定 
    # A
    bAoff = font1.render("Button A OFF", True, (0,0,0))
    # B
    bBoff = font1.render("Button B OFF", True, (0,0,0))
    # X
    bXoff = font1.render("Button X OFF", True, (0,0,0))
    # Y
    bYoff = font1.render("Button Y OFF", True, (0,0,0))
    # -
    bMINUSoff = font1.render("Button - OFF", True, (0,0,0))
    # home
    bHOMEoff = font1.render("Button HOME OFF", True, (0,0,0))
    # +
    bPLUSoff = font1.render("Button + OFF", True, (0,0,0))
    # L JOY
    bL_JOYoff = font1.render("Button L JOY OFF", True, (0,0,0))
    # R JOY
    bR_JOYoff = font1.render("Button R JOY OFF", True, (0,0,0))
    # L
    bLoff = font1.render("Button R OFF", True, (0,0,0))
    # R
    bRoff = font1.render("Button R OFF", True, (0,0,0))
    # UP
    bUPoff = font1.render("Button UP OFF", True, (0,0,0))
    # DOWN
    bDOWNoff = font1.render("Button DOWN OFF", True, (0,0,0))
    # LEFT
    bLEFToff = font1.render("Button LEFT OFF", True, (0,0,0))
    # RIGHT
    bRIGHToff = font1.render("Button RIGHT OFF", True, (0,0,0))
    # SHOT
    bSHOToff = font1.render("Button SHOT OFF", True, (0,0,0))
    screen.blit(bAoff, (t1, tt))
    screen.blit(bBoff, (t1, tt + 20))
    screen.blit(bXoff, (t1, tt + 40))
    screen.blit(bYoff, (t1, tt + 60))
    screen.blit(bMINUSoff, (t1, tt + 80))
    screen.blit(bHOMEoff, (t1, tt + 100))
    screen.blit(bPLUSoff, (t2, tt))
    screen.blit(bL_JOYoff, (t2, tt + 20))
    screen.blit(bR_JOYoff, (t2, tt + 40))
    screen.blit(bLoff, (t2, tt + 60))
    screen.blit(bRoff, (t2, tt + 80))
    screen.blit(bUPoff, (t2, tt + 100))
    screen.blit(bDOWNoff, (t3, tt))
    screen.blit(bLEFToff, (t3, tt + 20))
    screen.blit(bRIGHToff, (t3, tt + 40))
    screen.blit(bSHOToff, (t3, tt + 60))

def button_status_show_on(joystick, screen, accent_color, text_start1, text_start2, text_start3, text_top):
    font1 =pygame.font.SysFont("arial", 20) # フォント設定 
    # A
    bAon = font1.render("Button A ON", True, (0,0,0))
    # B
    bBon = font1.render("Button B ON", True, (0,0,0))
    # X
    bXon = font1.render("Button X ON", True, (0,0,0))
    # Y
    bYon = font1.render("Button Y ON", True, (0,0,0))
    # -
    bMINUSon = font1.render("Button - ON", True, (0,0,0))
    # home
    bHOMEon = font1.render("Button HOME ON", True, (0,0,0))
    # +
    bPLUSon = font1.render("Button + ON", True, (0,0,0))
    # L JOY
    bL_JOYon = font1.render("Button L JOY ON", True, (0,0,0))
    # R JOY
    bR_JOYon = font1.render("Button R JOY ON", True, (0,0,0))
    # L
    bLon = font1.render("Button L ON", True, (0,0,0))
    # R
    bRon = font1.render("Button R ON", True, (0,0,0))
    # UP
    bUPon = font1.render("Button UP ON", True, (0,0,0))
    # DOWN
    bDOWNon = font1.render("Button DOWN ON", True, (0,0,0))
    # LEFT
    bLEFTon = font1.render("Button LEFT ON", True, (0,0,0))
    # RIGHT
    bRIGHTon = font1.render("Button RIGHT ON", True, (0,0,0))
    # SHOT
    bSHOTon = font1.render("Button SHOT ON", True, (0,0,0))
    #A
    if joystick.get_button(0): 
        screen.fill(accent_color, (text_start1,text_top,150,20))
        screen.blit(bAon, (text_start1, text_top))
    #B
    elif joystick.get_button(1):
        screen.fill(accent_color, (text_start1,text_top + 20,150,20))
        screen.blit(bBon, (text_start1, text_top + 20))
    #X
    elif joystick.get_button(2):
        screen.fill(accent_color, (text_start1,text_top + 40,150,20))
        screen.blit(bXon, (text_start1, text_top + 40))
    #Y
    elif joystick.get_button(3):
        screen.fill(accent_color, (text_start1,text_top + 60,150,20))
        screen.blit(bYon, (text_start1, text_top + 60))
    #-
    elif joystick.get_button(4):
        screen.fill(accent_color, (text_start1,text_top + 80,150,20))
        screen.blit(bMINUSon, (text_start1, text_top + 80))
    #HOME
    elif joystick.get_button(5):
        screen.fill(accent_color, (text_start1,text_top + 100,150,20))
        screen.blit(bHOMEon, (text_start1, text_top + 100))

    #+
    elif joystick.get_button(6):
        screen.fill(accent_color, (text_start2,text_top,150,20))
        screen.blit(bPLUSon, (text_start2, text_top))
    #L JOY
    elif joystick.get_button(7):
        screen.fill(accent_color, (text_start2,text_top + 20,150,20))
        screen.blit(bL_JOYon, (text_start2, text_top + 20))
    #R JOY
    elif joystick.get_button(8):
        screen.fill(accent_color, (text_start2,text_top + 40,150,20))
        screen.blit(bR_JOYon, (text_start2, text_top + 40))
    #L
    elif joystick.get_button(9):
        screen.fill(accent_color, (text_start2,text_top + 60,150,20))
        screen.blit(bLon, (text_start2, text_top + 60))
    #R
    elif joystick.get_button(10):
        screen.fill(accent_color, (text_start2,text_top + 80,150,20))
        screen.blit(bRon, (text_start2, text_top + 80))
    #UP
    elif joystick.get_button(11):
        screen.fill(accent_color, (text_start2,text_top + 100,150,20))
        screen.blit(bUPon, (text_start2, text_top + 100))
    #DOWN
    elif joystick.get_button(12):
        screen.fill(accent_color, (text_start3,text_top,150,20))
        screen.blit(bDOWNon, (text_start3, text_top))
    #LEFT
    elif joystick.get_button(13):
        screen.fill(accent_color, (text_start3,text_top + 20,150,20))
        screen.blit(bLEFTon, (text_start3, text_top + 20))
    #RIGHT
    elif joystick.get_button(14):
        screen.fill(accent_color, (text_start3,text_top + 40,150,20))
        screen.blit(bRIGHTon, (text_start3, text_top + 40))
    #SHOT
    elif joystick.get_button(15):
        screen.fill(accent_color, (text_start3,text_top + 60,150,20))
        screen.blit(bSHOTon, (text_start3, text_top + 60))
