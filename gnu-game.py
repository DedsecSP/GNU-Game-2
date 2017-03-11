import pygame
import sys
from button import button
from pygame.locals import *
import pyganim

pygame.init()
windowWidth = 960
windowHeight = 540
title = "GNU Game 2.0"
windowSurface = pygame.display.set_mode((windowWidth, windowHeight), 0, 32)
pygame.display.set_caption('GNU Game 2.0')

pygame.font.init()
gameFont = pygame.font.SysFont("Times New Roman", 50, 1)

playGame = button((windowWidth/3)-len(title)+100, 250, 50, (0,0,0), (255,255,255), "Play Game", 25)
playGame.setClickedAction(print)
playGame.clicked()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    windowSurface.fill((255, 255, 255))
    label = gameFont.render(title, 1, (0,0,0))
    windowSurface.blit(label, ((windowWidth/3)-len(title),(windowHeight/3)-50))    
    pygame.draw.rect(windowSurface, playGame.color, (playGame.x, playGame.y, playGame.width, playGame.length))
    playGame.setFont()
    windowSurface.blit(playGame.label, (playGame.x+10, playGame.y))
    playGame.isHovered()
    
    
    pygame.display.update()
