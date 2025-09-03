#Colorful sprite
import pygame
import random
pygame.init()
SPRITE_COLOR_CHANGE_EVENT= pygame.USEREVENT+1
BACKGROUND_COLOR_CHANGE_EVENT= pygame.USEREVENT+2
BLUE= pygame.Color("blue")
PURPLE= pygame.Color("purple")
GREEN= pygame.Color("green")
#sprite color
YELLOW= pygame.Color("yellow")
AQUAMARINE= pygame.Color("aquamarine")
MAGENTA= pygame.Color("magenta")

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
        self.image= pygame.Surface([height, width])
        self.image.fill(color)
        self.rect= self.image.get_rect()
        self.velocity=[random.choice([-1,1]), random.choice([-1,1])]