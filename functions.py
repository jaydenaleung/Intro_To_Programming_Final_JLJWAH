import pygame
import classes

'''
Library of all functions. Does not include class methods; use 'import classes' to access those methods.
To access the functions here in another file, use 'import functions'.

- Joza, Amie, Jayden: Intro to Programming Fall 2024
'''

def quitCheck(event,running):
    if event.type == pygame.QUIT:
        running = False
    return running

def moveCheck(event,player,enemy):
    # Reset some important values
    player.falling = True
    enemy.falling = True
    
    if event.type == pygame.KEYDOWN: # WASD / arrow keys
        # Player
        if event.key == pygame.K_a: # move left
            player.movingLeft = True

        if event.key == pygame.K_d: # move right
            player.movingRight = True
        
        if event.key == pygame.K_w: # move up
            player.jumping = True
            player.jumpSpeed = 25.0
            player.gravMultiplier = 1
        


        # Enemy
        if event.key == pygame.K_LEFT: # move left
            enemy.movingLeft = True

        if event.key == pygame.K_RIGHT: # move right
            enemy.movingRight = True
        
        if event.key == pygame.K_UP: # move up
            enemy.jumping = True
            enemy.jumpSpeed = 25.0
            enemy.gravMultiplier = 1
        
  
    elif event.type == pygame.KEYUP:
        player.movingLeft = False
        player.movingRight = False
    

        enemy.movingLeft = False
        enemy.movingRight = False
  
    
    if event.type == pygame.MOUSEBUTTONUP:
        print(str(pygame.mouse.get_pos()[0]) + "," + str(pygame.mouse.get_pos()[1]))
