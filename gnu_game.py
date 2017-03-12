import pygame
import sys
import os
from button import button
from pygame.locals import *
import pyganim
from state_machine import Game
import yaml
from scroll_area import scrollArea

def startGame(FST):
    FST.clickedPlay()

def showOptions(FST):
    FST.clickedOptions()

if __name__ == "__main__":
    pygame.init()
    windowWidth = 960
    windowHeight = 540
    title = "GNU Game 2.0"
    windowSurface = pygame.display.set_mode((windowWidth, windowHeight), 0, 32)
    pygame.display.set_caption('GNU Game 2.0')
    pygame.font.init()

    # Initialize the game's state machine
    gnuGame = Game()

    # Initialize buttons
    fontName = "Times New Roman"
    gameFont = pygame.font.SysFont(fontName, 50, 1)
    characterFont = pygame.font.SysFont(fontName, 25, 1)
    
    text = "Play Game"
    playGame = button((windowWidth/3)-len(title)+100, 250, len(text)*(0.6 * 25), 30, (0,0,0), (255,255,255), text, 25)
    playGame.setClickedAction(startGame)
    
    text = "Options"
    options = button((windowWidth/3)-len(title)+100, 300, len(text)*(0.6 * 25), 30, (0,0,0), (255,255,255), text, 25)
    options.setClickedAction(showOptions)

    # Initialize character selection area
    s = scrollArea(100, 200, 200, 350)

    # Load character sprites
    config = {}
    for directory in os.listdir(".\\data\\characters"):
        print(directory)
        document = open(".\data\\characters\\%s\\config.yaml" % directory)
        data = yaml.safe_load(document)
        config[data["name"]] = data
        document.close()
    
    # Start the game
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        if gnuGame.state == "mainMenu":
            # Fill background color for the window
            windowSurface.fill((255, 255, 255))

            # Draw the game title on screen
            label = gameFont.render(title, 1, (0,0,0))
            windowSurface.blit(label, ((windowWidth/3)-len(title),(windowHeight/3)-50))    

            # Draw the "Play Game" button on screen
            pygame.draw.rect(windowSurface, playGame.color, (playGame.x, playGame.y, playGame.width, playGame.length))
            playGame.setFont(fontName)
            windowSurface.blit(playGame.label, (playGame.x+10, playGame.y))

            # Draw the "Options" button on screen
            pygame.draw.rect(windowSurface, options.color, (options.x, options.y, options.width, options.length))
            options.setFont(fontName)
            windowSurface.blit(options.label, (options.x+10, options.y))

            # Check to see if the buttons are interacted with
            playGame.isHovered()
            playGame.isClicked(gnuGame)

            options.isHovered()
            options.isClicked(gnuGame)
            
        elif gnuGame.state == "characterSelection":
            # Fill background color for the window
            windowSurface.fill((255, 255, 255))

            s.render(windowSurface)

            # Draw the character selection scroll area and its contents
            for character in config:
                message = character
                label = characterFont.render(message, 1, (0,0,0))
                windowSurface.blit(label, (100,225))

            # Draw WIP text
            message = "SELECTION"
            label = gameFont.render(message, 1, (0,0,0))
            windowSurface.blit(label, ((windowWidth/3)-len(message)+65,100))

            # Draw the avatars and their box
            p1Avatar = pygame.image.load(".\data\\characters\\ballmer\\avatar.png")
            windowSurface.blit(p1Avatar, (100,50))
            pygame.draw.rect(windowSurface, (50,50,50), (100,50,100,100), 2)
            windowSurface.blit(p1Avatar, (760,50))
            pygame.draw.rect(windowSurface, (50,50,50), (760,50,100,100), 2)

            # Draw the rest of the interface
            pygame.draw.line(windowSurface, (0,0,0), (50, 200), (250, 200))
            pygame.draw.line(windowSurface, (0,0,0), (710, 200), (910, 200))

        elif gnuGame.state == "options":
            # Fill background color for the window
            windowSurface.fill((255, 255, 255))

            # Draw options heading
            message = "Options"
            label = gameFont.render(message, 1, (0,0,0))
            windowSurface.blit(label, ((windowWidth/3)-len(message),(windowHeight/3)-50))


        
        pygame.display.update()
