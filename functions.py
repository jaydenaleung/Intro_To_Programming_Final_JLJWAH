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
            player.jumpSpeed = 20.0
            player.gravMultiplier = 1

            if event.key == pygame.K_w and player.doubleJump == True:
                player.jumping = True
                player.doubleJump == False



        # Enemy
        if event.key == pygame.K_LEFT: # move left
            enemy.movingLeft = True

        if event.key == pygame.K_RIGHT: # move right
            enemy.movingRight = True
        
        if event.key == pygame.K_UP: # move up
            enemy.jumping = True
            enemy.jumpSpeed = 20.0
            enemy.gravMultiplier = 1
            if event.key == pygame.K_UP and enemy.doubleJump == True:
                enemy.jumping = True
                enemy.doubleJump == False
        
  
    elif event.type == pygame.KEYUP:
        player.movingLeft = False
        player.movingRight = False
    

        enemy.movingLeft = False
        enemy.movingRight = False
  
    
    if event.type == pygame.MOUSEBUTTONUP:
        print(str(pygame.mouse.get_pos()[0]) + "," + str(pygame.mouse.get_pos()[1]))

def animationCheck(character): #doesn't work
    left = 0
    if character.direction and character.movingLeft:
        character.update(character.chosenCharacter.imagePaths[left])
        left+=1
        if left == len(character.chosenCharacter.imagePaths)/2:
            left = 0
    right = len(character.chosenCharacter.imagePaths)/2
    if character.direction == False and character.movingRight:
        character.update(character.chosenCharacter.imagePaths[right])
        right+=1
        if right == len(character.chosenCharacter.imagePaths):
            right = len(character.chosenCharacter.imagePaths)/2
            
def attackCheck(event,player,enemy):
    if event.type == pygame.KEYDOWN:
        movesP = player.chosenCharacter.moves
        for move in movesP:
            if move == 'melee':
                pass # moves to come
            elif move == 'ranged':
                pass # moves to come
            elif move == 'support': # more moves to come
                if event.key == pygame.K_q:
                    player.move1Activated = not player.move1Activated
                    player.move1 = 'support'

        movesE = enemy.chosenCharacter.moves
        for move in movesE:
            if move == 'melee': # moves to come  
                pass
            elif move == 'ranged': # moves to come
                pass
            elif move == 'support': # more moves to come
                if event.key == pygame.K_n:
                    enemy.move1Activated = not enemy.move1Activated
                    enemy.move1 = 'support'
