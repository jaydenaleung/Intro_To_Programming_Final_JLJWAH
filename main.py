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

# Background
background = "white"

# CLASS OBJECTS (CHARACTERS)
player = classes.Player(300,300,"assets\example_player.png")

# EXAMPLE CODE FOR SCENE (WILL REMOVE LATER)
example_background = pygame.image.load("assets\example_battlefield.png")
# Top Platform: (550,102),(733,124) - topleft,bottomRight

while running:
    # SETUP
    screen.fill(background)
    screen.blit(example_background,(0,0))


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

    
    if player.movingLeft and player.x >= 0: # Movement logic - without this, it will only move once when pressed and not when pressed down
        if (not (player.x > 550 and player.x < 733 and player.y > 102-player.sizey and player.y < 124)): # Top platform/example
            player.x -= player.speed
            if player.x > 550 and player.x <= 733 and player.y > 102-player.sizey and player.y < 124:
                player.x = 733
    if player.movingRight and player.x + player.sizex <= resX: # playerImg.get_size()[0] gets the horizontal size of the player
        if (not (player.x + player.sizex > 550 and player.x < 733 and player.y > 102-player.sizey and player.y < 124)):
            player.x += player.speed
            if player.x < 733 and player.x + player.sizex >= 550 and player.y > 102-player.sizey and player.y < 124:
                player.x = 550-player.sizex
    if player.movingUp and player.y >= 0:
        if (not (player.y > 102 and player.y < 124 and player.x > 550-player.sizex and player.x < 733)):
            player.y -= player.speed
            if player.y <= 124 and player.y > 102 and player.x > 550-player.sizex and player.x < 733:
                player.y = 125
    if player.movingDown and player.y + player.sizey <= resY:
        if (not (player.y + player.sizey > 102 and player.y < 124 and player.x > 550-player.sizex and player.x < 733)):
            player.y += player.speed
            if player.y < 124 and player.y + player.sizey >= 102 and player.x > 550-player.sizex and player.x < 733:
                player.y = 101-player.sizey


    # RENDER GAME OBJECTS HERE 
    player.update(screen)

    # UPDATE SCREEN
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60

pygame.quit()
