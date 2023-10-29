import pygame, random
from car import Car
pygame.init()

GREEN = (20,255,140)
GREY = (210,210,210)
WHITE = (255,255,255)
RED = (255,0,0)
PURPLE = (255,0,255)

SCREENWIDTH = 500
SCREENHEIGHT = 350

#Thiet lap kich thuoc cua so
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Car Racing")

all_sprites_list = pygame.sprite.Group()
playerCar = Car(RED,20,30)
playerCar.rect.x = 200
playerCar.rect.y = 300

all_sprites_list.add(playerCar)

carryOn = True

clock = pygame.time.Clock()

while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn=False

    screen.fill(GREEN)
    pygame.draw.rect(screen, GREY, [40,0,400,300])
    pygame.draw.line(screen,WHITE,[140,0],[140,300],5)
    pygame.draw.line(screen,WHITE,[240,0],[240,300],5)
    pygame.draw.line(screen,WHITE,[340,0],[340,300],5)

    all_sprites_list.draw(screen)

    pygame.display.flip()
    clock.tick(60)
pygame.quit()