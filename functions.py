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
        
        if event.key == pygame.K_w and player.doubleJump < 2: # move up
            player.jumping = True
            player.jumpSpeed = 20.0
            player.gravMultiplier = 1
            player.doubleJump += 1

        # Enemy
        if event.key == pygame.K_LEFT: # move left
            enemy.movingLeft = True

        if event.key == pygame.K_RIGHT: # move right
            enemy.movingRight = True
        
        if event.key == pygame.K_UP and enemy.doubleJump < 2: # move up
            enemy.jumping = True
            enemy.jumpSpeed = 20.0
            enemy.gravMultiplier = 1
            enemy.doubleJump += 1
        
  
    elif event.type == pygame.KEYUP:
        player.movingLeft = False
        player.movingRight = False
    

        enemy.movingLeft = False
        enemy.movingRight = False
  
    
    if event.type == pygame.MOUSEBUTTONUP:
        print(str(pygame.mouse.get_pos()[0]) + "," + str(pygame.mouse.get_pos()[1]))

def animationCheck(event,character,player): #doesn't work JAYDEN HEREEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
    #if event.type == pygame.KEYDOWN:
    left = 0
    right = right = len(character.chosenCharacter.imagePaths)/2

    #left
    if event.type == pygame.K_LEFT or pygame.K_a:
        print("left")
        left+=1
        character.image = player.chosenCharacter.images[left]
    else:
        left = 0 

    if left == len(character.chosenCharacter.imagePaths)/2:
        left = 0

    else:
        left = 0

    '''
    #right
    if event.type == pygame.K_RIGHT or pygame.K_d:
        if event.type == pygame.K_LEFT or pygame.K_a:
            print("right")
            right+=1
            character.image = player.chosenCharacter.images[right]
    else:
        right = 0 
    if right == len(character.chosenCharacter.imagePaths):
        right = len(player.chosenCharacter.images)/2
    
    else:
        right = 0
    '''

def attackCheck(event,player,enemy):
    if event.type == pygame.KEYDOWN:
        movesP = player.chosenCharacter.moves
        for move in movesP:
            if move == 'melee':
                if event.key == pygame.K_x:
                    player.move2Activated = not player.move1Activated
                    player.move2 = 'melee'
            elif move == 'ranged':
                pass # moves to come
            elif move == 'support': # more moves to come
                if event.key == pygame.K_z:
                    player.move1Activated = not player.move1Activated
                    player.move1 = 'support'

        movesE = enemy.chosenCharacter.moves
        for move in movesE:
            if move == 'melee': # moves to come  
                if event.key == pygame.K_m:
                    enemy.move2Activated = not enemy.move2Activated
                    enemy.move2 = 'melee'
            elif move == 'ranged': # moves to come
                pass
            elif move == 'support': # more moves to come
                if event.key == pygame.K_n:
                    enemy.move1Activated = not enemy.move1Activated
                    enemy.move1 = 'support'
