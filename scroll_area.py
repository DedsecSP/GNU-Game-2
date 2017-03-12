from button import button
import pygame

class scrollArea:
    def __init__(self, x=0, y=0, width=100, length=200, scrollBarWidth=20):
        self.x = x
        self.y = y
        self.width = width
        self.length = length
        self.contentY = 0
        self.scrollBarWidth = scrollBarWidth
        self.scrollPadding = 2
        self.buttonX = abs((self.x+self.width) - self.scrollBarWidth)
        self.buttonY = self.y+self.scrollPadding
        self.button = button(self.buttonX, self.buttonY, scrollBarWidth, 30, (25,25,25), (25,25,25))
        self.button.setClickedAction = self.moveScrollBar

    def scrollUp(self):
        if self.contentY > 0:
            self.contentY -= 10

    def scrollDown(self):
        self.contentY += 10

    def render(self, screen):
        if self.button.isClicked():
            print("asdads")
            
        pygame.draw.rect(screen, self.button.color, (self.button.x, self.button.y, self.button.width, self.button.length))

    
