from Player import Player
import pygame as py
py.init()
width, height = 600, 600
screen = py.display.set_mode((width, height))
py.display.set_caption("Movement")
clock = py.time.Clock()

run = True
#Setting up the background colour

player1 = Player(0, 0)


x, y = width/2, height/2
speedX, speedY = 3, 5
player2 = Player(x, y)
c = "#A1B4D6" #colour
while run:
    for event in py.event.get():
        if event.type == py.QUIT:
            run = False
    clock.tick(60)
    screen.fill("#e2dede")
    r1 = player1.draw(screen)            #this will call the draw function from Player
    r2 = player2.draw(screen)
    player1.move(screen)
    # player1.collision(player2)
    '''
    colliderect(rect) detects collision between 2 rect objects.
    It returns true or false.
    '''
    print(r1.colliderect(r2))

    '''
    We want to detect collision with another Rect object of pygame.

    '''

    py.display.flip()

py.quit()