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

def moveCheck(event,characters):
    for character in characters:
        if event.type == pygame.KEYDOWN: # WASD / arrow keys
            if event.key == pygame.K_LEFT or event.key == pygame.K_a: # move left
                character.movingLeft = True

            if event.key == pygame.K_RIGHT or event.key == pygame.K_d: # move right
                character.movingRight = True
            
            if event.key == pygame.K_UP or event.key == pygame.K_w: # move up
                character.movingUp = True
            
            if event.key == pygame.K_DOWN or event.key == pygame.K_s: # move down
                character.movingDown = True
        elif event.type == pygame.KEYUP:
            character.movingLeft = False
            character.movingRight = False
            character.movingUp = False
            character.movingDown = False
        
        if event.type == pygame.MOUSEBUTTONUP:
            print(str(pygame.mouse.get_pos()[0]) + "," + str(pygame.mouse.get_pos()[1]))