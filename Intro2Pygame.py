import pygame as py
py.init()
width, height = 600, 600

# python -m pip install pygame

#the below statement creates a screen of a given size
screen = py.display.set_mode((width, height))
#changing caption of the screen
py.display.set_caption("Intro to Pygame")

#the event part of the code makes the window visible
#waits for us to close the window
screen.fill("#bdd2ac")
listCord = [(0, 600), (width/2, height/2), (600, 0), (600, 600), (width/2, height/2)]
run = True
#we need clock object to write effient and resource conserving program.
clock = py.time.Clock()
while run:
    #this is needed to identify when quit is pressed
    for event in py.event.get():
        if event.type == py.QUIT:
            run = False
    clock.tick(60)
    py.draw.line(screen,"#ff0000", (0,0), (width/2, height/2))
    # py.draw.lines(screen,"#00ff00", False,listCord)
    py.draw.line(screen,"#2139f5", (600,0), (width/2, height/2), 2)
    py.draw.line(screen,"#15ff00", (0,600), (width/2, height/2), 3)
    py.draw.line(screen,"#3a2f2f", (600,600), (width/2, height/2), 4)
    # py.draw.lines()

    #we want to draw rectangle, circle and ellipse
    py.draw.rect(screen, "#bebef7",(250, 250, 100, 100))
    #       canvas, color, rectangle(x-pos, y-pos, width, height)
    py.draw.circle(screen, "#827F7F", (300, 500), 75)
    #              canvas, color, (x-pos, y-pos), radius
    py.draw.ellipse(screen, "#ffff00", (125, 250, 50, 100))
    #canvas, color, (x-pos of top left, y-poz of top left, width, height)
    py.draw.ellipse(screen, "#ffff00", (425, 250, 50, 100))
    py.draw.ellipse(screen, "#a8a816", (200, 50, 200, 100))
    py.draw.circle(screen, "#000000", (150, 300),25,5)
    py.draw.circle(screen, "#000000", (450, 300),25,5)
    
    #update the screen
    py.display.flip()

py.quit()

