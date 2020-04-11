import pygame
import sys
import random

BLUE = (0,0,255)
RED = (255,0,0)

pygame.init()

# Set screen info
WIDTH = 900
HEIGHT = 700
size = (WIDTH,HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.update()

game_over = False

score = 0

RAINSIZE = 50
rain_list = []

SPEED = 50
AMOUNT = 10
