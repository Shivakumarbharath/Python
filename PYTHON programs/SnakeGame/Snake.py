import math
import random
import pygame
import tkinter as tK
from tkinter  import messagebox

pygame.init()

width=500

rows=20
class cube(object):
    rows=0
    columns=0
    def __init__(self,start,drx=1,dry=0,colour=(255,0,0)):
        pass


    def move(self,drx,dry):
        pass

    def draw(self, surface,eyes=False):
        pass

class snake(object):
    body=[]  # the list of cubes becomes the body of snake
    turns={}

    def __init__(self,colour ,pos):
        self.colour=colour
        self.head=cube(pos)
        self.body.append(self.head)# to add multiple cubes in the list of body
        self.drx=0# direction of x and
        self.dry=1# direction for y



    def move(self):
        for event in pygame.event.get():  # to quit when Close button is clicked
            if event.type == pygame.QUIT:
                pygame.quit()

        keys=pygame.key.get_pressed()# returns a list
        for key in keys:
            if (keys[pygame.K_LEFT]):  #eqvuivalent topygame.key.get_pressed(pygame.K_LEFT)
                self.drx=-1
                self.dry=0
                self.turns[self.head.pos[:]] = [self.drx, self.dry]  # to store the place where the turn takes place

            elif(keys[pygame.K_RIGHT]):
                self.drx = 1 # in the direction of taking the turn
                self.dry = 0
                self.turns[self.head.pos[:]]=[self.drx,self.dry] # to store the place where the turn takes place


            elif (keys[pygame.K_UP]):
                self.drx = 0
                self.dry = 1
                self.turns[self.head.pos[:]] = [self.drx, self.dry]  # to store the place where the turn takes place

            elif(keys[pygame.K_DOWN]):
                self.drx = 0
                self.dry = -1
                self.turns[self.head.pos[:]] = [self.drx, self.dry]  # to store the place where the turn takes place




    def reset(self,pos):
        pass

    def addcube(self):
        pass

    def draw(self,surface):
        pass


def DrawGrid(width,rows,surface):
    sizebtw=width//rows # the size of the squares in grid
    x=0
    y=0
    for i in range(rows):
        x+=sizebtw
        y += sizebtw
        pygame.draw.line(surface,(255,255,255),(x,0),(x,width))# draw a line on the surface in white colour from position x,0 to x,width
        pygame.draw.line(surface, (255, 255, 255), (0, y),(width, y))  # draw a line on the surface in white colour from position 0,y to width,y


def redrawWindow(surface):
    global width, rows #to make the variables global
    surface.fill((0,0,0)) #for black surface
    DrawGrid(width,rows,surface) # to drae a grid
    pygame.display.update() # to update the surface

def RandomSnack(rows,items):
    pass

# def messagebox(subject,content):
#     pass

def main():

    win=pygame.display.set_mode((width,width))  #to make a window
    pygame.display.set_caption('Snake 123')  # Yeah, exactly :)
    s=snake((255,0,0),(10,10))  #to create a snake object with colour and position
    clock=pygame.time.Clock()



    while True:


        pygame.time.delay(50)# so that program does not run too fast ;lower it is gamee is faster
        clock.tick(10)# so that game run within 10 frames per second i.e snake can move 10 blocks per second
        # lower it slower the game

        redrawWindow(win)  # here the surface of game is win

main()




