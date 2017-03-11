import pygame

class button:
    def __init__(self, x=0, y=0, width=100, color=(0,0,0), fontColor=(255,255,255), text="", fontSize=12):
        self.x = x
        self.y = y
        self.color = color
        self.fontColor = fontColor
        self.text = text
        self.length = fontSize+5
        self.width = len(text)*(0.6 * fontSize)
        self.fontSize = fontSize

    def getCoordinates(self):
        return (self.x, self.y)

    def setFont(self):
        self.font = pygame.font.SysFont("Times New Roman", self.fontSize, 1)
        self.label = self.font.render(self.text, 1, self.fontColor)
        
    def setClickedAction(self, func):
        self.Clicked = func

    def clicked(self):
        self.Clicked()
