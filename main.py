import pygame
import classes
import functions

'''
RUN THE PROGRAM HERE. Main file which connects and compiles all the different frameworks and mechanics. Enjoy!

- Joza, Amie, Jayden: Intro to Programming Fall 2024
'''
脑子 = "not found"

# Start Pygame
pygame.init()
resX = 1280; resY = 720
screen = pygame.display.set_mode((resX, resY))
clock = pygame.time.Clock()
running = True

title = "Super Smash Bros. X (ITP 2024)"
icon = pygame.image.load("assets\icon.png")
pygame.display.set_caption(title)
pygame.display.set_icon(icon)

# Setup
background = "white"

# Characters/player animations
mario = classes.Character(
    # Animations
    ["assets\characters\example_char.png"],

    # Moves
    [classes.Shield(screen),
     classes.Punch(screen,5)]
)

amogus = classes.Character(
    # Animations
    ["assets\characters\AmongUs\Among_us_left1.png", 
    "assets\characters\AmongUs\Among_us_left2.png", 
    "assets\characters\AmongUs\Among_us_left2.5.png", 
    "assets\characters\AmongUs\Among_us_left3.png", 
    "assets\characters\AmongUs\Among_us_left4.png", 
    "assets\characters\AmongUs\Among_us_left5.png", 
    "assets\characters\AmongUs\Among_us_left6.png", 
    "assets\characters\AmongUs\Among_us_left7.png", 
    "assets\characters\AmongUs\Among_us_left8.png",

    "assets\characters\AmongUs\Among_us_right1.png",
    "assets\characters\AmongUs\Among_us_right2.png", 
    "assets\characters\AmongUs\Among_us_right2.5.png", 
    "assets\characters\AmongUs\Among_us_right3.png", 
    "assets\characters\AmongUs\Among_us_right4.png", 
    "assets\characters\AmongUs\Among_us_right5.png", 
    "assets\characters\AmongUs\Among_us_right6.png", 
    "assets\characters\AmongUs\Among_us_right7.png", 
    "assets\characters\AmongUs\Among_us_right8.png"],
    # Moves (classes with method execute() to use them)
    [classes.Shield(screen),
     classes.Punch(screen,5)]
)

characters = [mario,amogus] # more to come

# CLASS OBJECTS
spawnX1 = 280; spawnY1 = 294; spawnX2 = 970; spawnY2 = 294
player = classes.Player(spawnX1,spawnY1,characters[0])
enemy = classes.Enemy(spawnX2,spawnY2,characters[1])
players = [player,enemy]

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

if 脑子 == "smart":
    脑子 = "Found"

while running:
    # SETUP
    screen.fill(background)
    scene.update(screen)


    # WATCH FOR EVENTS HERE (CONDITIONALS SECTION)
    for event in pygame.event.get(): # BUG: this loop only runs when there are events, not always.
        running = functions.quitCheck(event,running)
        functions.moveCheck(event,players[0],players[1])
        functions.attackCheck(event,players[0],players[1])
        functions.animationCheck(event,players[0],player)
    
    for character in players:
        for barrier in barriers:
            barrier.solidify(screen,character)


    # RENDER GAME OBJECTS HERE
        character.update(screen,character,players)

    # UPDATE SCREEN
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60

pygame.quit()
