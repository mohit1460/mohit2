import pygame
pygame.init()
width=800
height=600
black=(0,0,0)
white=(255,255,255)
gamedisplay=pygame.display.set_mode((width,height))
pygame.display.set_caption('race3')
clock=pygame.time.Clock()
carimg=pygame.image.load("car.png")
def car(x,y):
    gamedisplay.blit(carimg,(x,y))
x=(width*0.40)
y=(height*0.75)
xchange=0

crash=False
while not crash:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crash=True
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_LEFT:
                xchange=-5
            if event.type == pygame.K_RIGHT:
                xchange=5
        if event.type == pygame.KEYUP:
            if event.type == pygame.K_RIGHT or event.type == pygame.K_LEFT:
                xchange=0


    x=x+xchange
    gamedisplay.fill(white)
    car(x,y)
    pygame.display.update()
    clock.tick(60)
pygame.QUIT
quit()

