import pygame

class button:
    def __init__(self, x=0, y=0, width=100, length=10, color=(0,0,0), fontColor=(255,255,255), text="", fontSize=12):
        self.x = x
        self.y = y
        self.color = color
        self.baseColor = color
        self.fontColor = fontColor
        self.text = text
        self.length = length
        self.width = width
        self.fontSize = fontSize

    def getCoordinates(self):
        return (self.x, self.y)

    def setFont(self, fontName):
        self.font = pygame.font.SysFont(fontName, self.fontSize, 1)
        self.label = self.font.render(self.text, 1, self.fontColor)
        
    def setClickedAction(self, func):
        self.Clicked = func

    def isClicked(self, FST=""):
        mouse = pygame.mouse.get_pressed()
        if self.isHovered() and mouse[0] == 1:
            self.Clicked(FST)
            return True

    def isHovered(self):
        self.hoverColor = (abs(self.baseColor[0]-80), abs(self.baseColor[1]-80), abs(self.baseColor[2]-80))

        mouse = pygame.mouse.get_pos()
        if (self.x <= mouse[0] <= self.x+self.width) and (self.y <= mouse[1] <= self.y+self.length):
            self.color = self.hoverColor
            return True
        else:
            self.color = self.baseColor
            return False
