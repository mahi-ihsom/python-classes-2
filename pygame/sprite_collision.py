import pygame
import random
screen_width, screen_height= 500,400
movement_speed= 5
font_size= 72
pygame.init()
bg_image= pygame.transform.scale(pygame.image.load("bg.jpg"), (screen_width, screen_height))
font= pygame.font.SysFont("Algerian", font_size)
class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
        self.image= pygame.Surface([width, height])
        self.image.fill(pygame.Color("Dark blue"))
        pygame.draw.rect(self.image,color, pygame.Rect(0,0,width,height))
        self.rect=self.image.get_rect()
    def move(self, x_change, y_change):
        self.rect.x=max(min(self.rect.x + x_change,screen_width-self.rect.width), 0)
        self.rect.y=max(min(self.rect.y + y_change,screen_height-self.rect.height), 0)
screen= pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sprite collision")
all_sprite= pygame.sprite.Group()
sprite1= Sprite(pygame.Color("black"), 20,30)
sprite1.rect.x,sprite1.rect.y= random.randint(0,screen_width-sprite1.rect.width),random.randint(0,screen_height-sprite1.rect.height)
all_sprite.add(sprite1)
sprite2= Sprite(pygame.Color("white"), 20,30)
sprite2.rect.x,sprite2.y= random.randint(0,screen_width-sprite2.rect.width),random.randint(0,screen_height-sprite2.rect.height)
all_sprite.add(sprite2)
running, won= True, False
clock= pygame.time.Clock()