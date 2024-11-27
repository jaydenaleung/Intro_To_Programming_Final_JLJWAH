import pygame
import classes
import functions

'''
RUN THE PROGRAM HERE. Main file which connects and compiles all the different frameworks and mechanics. Enjoy!

- Joza, Amie, Jayden: Intro to Programming Fall 2024
'''

# Start Pygame
pygame.init()
resX = 1280; resY = 720
screen = pygame.display.set_mode((resX, resY))
clock = pygame.time.Clock()
running = True

title = "Super Smash Bros. X (ITP 2024)"
icon = pygame.image.load("assets\icon.png")
pygame.display.set_caption(title)
pygame.display.set_icon(icon) # https://www.flaticon.com/free-icon-font/browser_3914451?page=1&position=1&term=programming&origin=search&related_id=3914451

# Setup
background = "white"

# CLASS OBJECTS
spawnX1 = 380; spawnY1 = 294; spawnX2 = 805; spawnY2 = 294
player = classes.Player(spawnX1,spawnY1,"assets\example_char.png")
enemy = classes.Player(spawnX2,spawnY2,"assets\example_enemy.png")
characters = [player,enemy]

scene = classes.Scene("assets\example_battlefield.png")
barrierT = scene.Barrier(550,102,733,124)
barrierL = scene.Barrier(340,218,528,238)
barrierR = scene.Barrier(756,218,944,237)
barrierM1 = scene.Barrier(252,355,1016,412)
#barrierM2 = scene.Barrier(311,317,913,458)
barrierM3 = scene.Barrier(375,461,890,484)
barrierM4 = scene.Barrier(435,494,772,546)
barrierM5 = scene.Barrier(587,555,711,657)
barriers = [barrierT,barrierL,barrierR,barrierM1,barrierM3,barrierM4,barrierM5]


while running:
    # SETUP
    screen.fill(background)
    scene.update(screen)


    # WATCH FOR EVENTS HERE (CONDITIONALS SECTION)
    for event in pygame.event.get():
        running = functions.quitCheck(event,running)
        functions.moveCheck(event,characters)
    
    for character in characters:
        for barrier in barriers:
            barrier.solidify(screen,character)


    # RENDER GAME OBJECTS HERE
        character.update(screen,character)


    # UPDATE SCREEN
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60

pygame.quit()
