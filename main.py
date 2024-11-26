import pygame
import classes

# Start Pygame
pygame.init()
resX = 1280; resY = 720
screen = pygame.display.set_mode((resX, resY))
clock = pygame.time.Clock()
running = True

title = "Super Smash Bros. by Intro To Programming Fall 2024"
icon = pygame.image.load("assets\icon.png")
pygame.display.set_caption(title)
pygame.display.set_icon(icon) # https://www.flaticon.com/free-icon-font/browser_3914451?page=1&position=1&term=programming&origin=search&related_id=3914451

# Setup
background = "white"

# CLASS OBJECTS
player = classes.Player(300,300,"assets\example_player.png")

scene = classes.Scene("assets\example_battlefield.png")
barrierT = scene.Barrier(550,102,733,124)
barrierL = scene.Barrier(340,218,528,238)
barrierR = scene.Barrier(756,218,944,237)
barrierM1 = scene.Barrier(252,355,1016,412)
barrierM2 = scene.Barrier(311,317,913,458)
barrierM3 = scene.Barrier(375,461,890,484)
barrierM4 = scene.Barrier(435,494,772,546)
barrierM5 = scene.Barrier(522,555,711,657)
barriers = [barrierT,barrierL,barrierR,barrierM1,barrierM2,barrierM3,barrierM4,barrierM5]


while running:
    # SETUP
    screen.fill(background)
    scene.update(screen)


    # WATCH FOR EVENTS HERE (CONDITIONALS SECTION)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN: # WASD / arrow keys
            if event.key == pygame.K_LEFT or event.key == pygame.K_a: # move left
                player.movingLeft = True

            if event.key == pygame.K_RIGHT or event.key == pygame.K_d: # move right
                player.movingRight = True
            
            if event.key == pygame.K_UP or event.key == pygame.K_w: # move up
                player.movingUp = True
            
            if event.key == pygame.K_DOWN or event.key == pygame.K_s: # move down
                player.movingDown = True
        elif event.type == pygame.KEYUP:
            player.movingLeft = False
            player.movingRight = False
            player.movingUp = False
            player.movingDown = False
        
        if event.type == pygame.MOUSEBUTTONUP:
            print(str(pygame.mouse.get_pos()[0]) + "," + str(pygame.mouse.get_pos()[1]))
    
    # for barrier in barriers:
    #     barrier.solidify(player,resX,resY)
    barrierT.solidify(player,resX,resY)


    # RENDER GAME OBJECTS HERE
    player.update(screen)


    # UPDATE SCREEN
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60

pygame.quit()
