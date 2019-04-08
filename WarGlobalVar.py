import random
import pygame
import sys
from pygame.locals import *

#---color setting------
WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
DARKGRAY = ( 40, 40, 40 )
DARKGREEN = ( 0, 155, 0 )
BGCOLOR = BLACK
#----------------------

RIGHT = "RIGHT"
LEFT = "LEFT"
UP = "UP"
DOWN = "DOWN"

#------GAME CONSTANT--------
FPS = 3
ArmyA_Status = {}
ArmyB_Status = {}
Hero_Status = {}
Army_A_Num = 10
Army_B_Num = 20
Army_A_Color = RED
Army_B_Color = GREEN
#-----Window setting--------
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
CELLSIZE = 20
assert WINDOWWIDTH % CELLSIZE == 0, "Window width must be a multiple of cell size."
assert WINDOWHEIGHT % CELLSIZE == 0, "Window height must be a multiple of cell size."
CELLWIDTH = int(WINDOWWIDTH / CELLSIZE)
CELLHEIGHT = int(WINDOWHEIGHT / CELLSIZE)
#---------------------------
