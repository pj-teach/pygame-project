from random import randint
import pygame as py
from Player import Player, Obstacle
py.mixer.init()
coin_sound = py.mixer.Sound("./GameProject/coins.mp3")
#to generalise our grid we use the following variables
grid_r, grid_c = 9,9
grid = [[randint(0,4) for i in range(grid_c)] for j in range(grid_r)]

# ensure starting area is always open
grid[0][0] = 1
grid[0][1] = 1  # right neighbour
grid[1][0] = 1  # bottom neighbour

for g in grid:
    print(g)
#todo - create panel, draw font surface, create coins and dug variables
#update the tiles based on if they received a coin or no coin

cell_size = 60 #cell size in which the player will reside
#width and height of the game layout depends on the grid and cell size
width, height = cell_size*grid_c, cell_size*grid_r
panel = 150
coins = 0
coinImg = py.image.load('./GameProject/chest.png')
coinImg = py.transform.scale(coinImg,(40,40))
pumpkin = py.image.load('./GameProject/pumpkin.jpg')
pumpkin = py.transform.scale(pumpkin,(60,60))
obstacleImg = py.image.load('./GameProject/obstacle1.png')
obstacleImg = py.transform.scale(obstacleImg,(60,60))
bgImg = py.image.load('./GameProject/bg1.png')
bgImg = py.transform.scale(bgImg,(width, height))
img = py.image.load('./GameProject/dog.png')
img = py.transform.scale(img,(60,60)) #scale the image
player1 = Player(0,0,img) #we need to pass img in the Player() constructor
#because this is how we redefined our class
#creating a list of obstacle object to be printed later.
obstacleList = []
for r in range(grid_r):
    for c in range(grid_c):
        if grid[r][c] == 0:
            obstacleList.append(Obstacle(c*cell_size, r*cell_size, obstacleImg))
            #there was issue here that r and c were swapped

py.init()
screen = py.display.set_mode((width+panel, height))
py.display.set_caption("Creating Grid")
clock = py.time.Clock() 

def draw_grid(grid:list):
    row = 0 #row of the grid
    col = 0 #column of the grid
    index = 0
    for i in range(grid_r*grid_c): #looping through the entire grid
        if grid[row][col] == 0:    #check if the grid list has 1
            #if yes then draw the obstacle
            obstacleList[index].draw(screen)
            index += 1
            # py.draw.rect(screen, "#000000", (row*cell_size, col*cell_size, cell_size, cell_size))
        elif grid[row][col] == 5:
            screen.blit(pumpkin,(col*cell_size, row*cell_size))
        elif grid[row][col] == 6:
            screen.blit(coinImg,(col*cell_size+10, row*cell_size+10))
        col += 1 #then go to the next cell
        if col == grid_c:   #if you reach the last column
            row += 1 #then we go to the next row
            col = 0 #and we reset the column to zero

def draw_panel(screen, coins):
    font = py.font.SysFont(None, 30)  
    # panel background
    py.draw.rect(screen, "#8BD0CA", (width, 0, panel, height))
    textSurface = font.render(f"Coins: {player1.coins}", True, "#ffffff")
    screen.blit(textSurface, (width + 20, 40))
    # screen.blit(font.render(f"Dug: {dug}", True, "#ffffff"), (width + 20, 80))
def dig():
    if event.type == py.KEYDOWN:
        if event.key == py.K_SPACE:
            r, c = player1.y//60, player1.x//60
            if grid[r][c] == 3:
                player1.coins += 1
                grid[r][c] = 6
                coin_sound.play()
                screen.blit(coinImg,(player1.x,player1.y))
            elif 1<= grid[r][c] <= 4:
                grid[r][c] = 5
                screen.blit(pumpkin,(player1.x,player1.y))


run = True
while run:
    clock.tick(10)
    for event in py.event.get():
        if event.type == py.QUIT:
            run = False
        #we use player move here because of event object inside the loop
        player1.move(screen, grid, event)
        dig()

    # screen.fill("#ffffff")
    screen.blit(bgImg,(0,0))#adds background image to the screen
    draw_panel(screen,coins)
    draw_grid(grid)
    player1.draw(screen)
    
       
    py.display.flip()#update the screen


py.quit()

