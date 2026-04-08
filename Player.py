import pygame as py
from dataclasses import dataclass
py.init()


class Player:
    '''
    Create a player with x, y coordinates
    and w, h as it's width and height
    '''
    #static variable/ class variables
    speedX , speedY = 5, 5
    collide = False
    #constructor
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.w = 50
        self.h = 50
        self.img = img
        self.coins = 0
        self.rect = (self.x, self.y, self.w, self.h)
    
    def draw(self, screen):
        #blit draws surface on a surface. Here image surface is drawn on the screen surface
        screen.blit(self.img, (self.x, self.y))
    
    def move(self, screen, grid, event):
        r = self.y // 60 #there was an issue here r and c were swapped
        c = self.x // 60
        if event.type == py.KEYDOWN:
            if event.key == py.K_LEFT and c - 1 >= 0 and grid[r][c-1] != 0:
                self.x -= 60
            if event.key == py.K_RIGHT and c + 1 < len(grid[0]) and grid[r][c+1] != 0:
                self.x += 60
            if event.key == py.K_UP and r - 1 >= 0 and grid[r-1][c] != 0:
                self.y -= 60
            if event.key == py.K_DOWN and r + 1 < len(grid) and grid[r+1][c] != 0:
                self.y += 60
            # if(grid[self.y//60][self.x//60] == 3):#condition to find a coint
            #     self.coins += 1 #if found increase the value by 1
                # grid[self.y//60][self.x//60] = 5   #we change the value in grid so that the coin will not be found repeatedly
            self.rect = (self.x, self.y, self.w, self.h)
    
    def collision(self, obstacle):
        if abs(self.x - obstacle.x) < self.w:
            if abs(self.y - obstacle.y) <self.h:
                if (not Player.collide):
                    print("Collision")
                    Player.collide = True
            else:
                Player.collide = False
        else:
            Player.collide = False    

#using dataclass is a standard for when the attributes/instance variables
#are straight forward
@dataclass          
class Obstacle:
    x: int
    y: int
    img:any
    #to be checked how to create static variable with dataclass
    def draw(self, screen):
        screen.blit(self.img,(self.x, self.y))