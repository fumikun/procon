import pygame
from pygame.locals import *

def Analog_status_reset(screen):
    pygame.draw.ellipse(screen, (0,0,0), (600, 225, 50, 50))
    pygame.draw.ellipse(screen, (0,0,0), (850, 225, 50, 50))

def Analog_status_show(pygame, joystick, sensitivity, screen, bgcolor):
    if abs((joystick.get_axis(0))) >= sensitivity or abs((joystick.get_axis(1))) >= sensitivity:
        pygame.draw.ellipse(screen, bgcolor, (600, 225, 50, 50))
        pygame.draw.ellipse(screen, (0,0,0), (625 + joystick.get_axis(0) * 125 -25, 250 + joystick.get_axis(1) * 125 -25, 50, 50))
        pygame.display.update()
    elif abs((joystick.get_axis(2))) >= sensitivity or abs((joystick.get_axis(3))) >= sensitivity:
        pygame.draw.ellipse(screen, bgcolor, (850, 225, 50, 50))
        pygame.draw.ellipse(screen, (0,0,0), (875 + joystick.get_axis(2) * 125 -25, 250 + joystick.get_axis(3) * 125 -25, 50, 50))
        pygame.display.update()
    if abs((joystick.get_axis(0))) <= sensitivity or abs((joystick.get_axis(1))) <= sensitivity:
        pygame.draw.ellipse(screen, (0,0,0), (500, 125, 250, 250), 5)
        pygame.display.update()
    elif abs((joystick.get_axis(2))) <= sensitivity or abs((joystick.get_axis(3))) <= sensitivity:
        pygame.draw.ellipse(screen, (0,0,0), (750, 125, 250, 250), 5)
        pygame.display.update()