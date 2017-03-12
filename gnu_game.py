import pygame
import sys
from button import button
from pygame.locals import *
import pyganim
from state_machine import Game

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
    gameFont = pygame.font.SysFont("Times New Roman", 50, 1)
    
    playGame = button((windowWidth/3)-len(title)+100, 250, 50, (0,0,0), (255,255,255), "Play Game", 25)
    playGame.setClickedAction(startGame)
    
    options = button((windowWidth/3)-len(title)+100, 300, 50, (0,0,0), (255,255,255), "Options", 25)
    options.setClickedAction(showOptions)

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
            playGame.setFont()
            windowSurface.blit(playGame.label, (playGame.x+10, playGame.y))

            # Draw the "Options" button on screen
            pygame.draw.rect(windowSurface, options.color, (options.x, options.y, options.width, options.length))
            options.setFont()
            windowSurface.blit(options.label, (options.x+10, options.y))

            # Check to see if the button is interacted with
            playGame.isHovered()
            playGame.isClicked(gnuGame)

            options.isHovered()
            options.isClicked(gnuGame)
            
        elif gnuGame.state == "playGame":
            # Fill background color for the window
            windowSurface.fill((255, 255, 255))

            # Draw WIP text
            message = "Sorry, WIP"
            label = gameFont.render(message, 1, (0,0,0))
            windowSurface.blit(label, ((windowWidth/3)-len(title),(windowHeight/3)-50))

        elif gnuGame.state == "options":
            # Fill background color for the window
            windowSurface.fill((255, 255, 255))

            # Draw options heading
            message = "Options"
            label = gameFont.render(message, 1, (0,0,0))
            windowSurface.blit(label, ((windowWidth/3)-len(title),(windowHeight/3)-50))
        
        pygame.display.update()
