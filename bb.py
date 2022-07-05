import sys
import pygame
import os       
pygame.init()  #to intialize the pygame
size=width,height=1000,800 
speed=[1,1]   #spped with which ball move
background=255,255,255
screen=pygame.display.set_mode(size) #tocreate the window/farme
pygame.display.set_caption("BOUNCING BALL")
ball=pygame.image.load("D:\Desktop\\bounce\\12321.jpeg")
ballrect=ball.get_rect()#ball in rect
while 1:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
    ballrect=ballrect.move(speed)
    if ballrect.left<0 or ballrect.right>width:
        speed[0]=-speed[0]
    if ballrect.top<0 or ballrect.bottom>height:
        speed[1]=-speed[1]
    screen.fill(background)
    screen.blit(ball,ballrect)
    pygame.display.flip()
