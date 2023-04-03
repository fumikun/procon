import pygame
from pygame.locals import *
import time

def Button_status(screen, t1, t2, t3, tt):
    font1 =pygame.font.SysFont("arial", 20) # フォント設定 
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
    bPLUSon = font1.render("Button + ON", True, (0,0,0))
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
    bUPoff = font1.render("Button UP OFF", True, (0,0,0))
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