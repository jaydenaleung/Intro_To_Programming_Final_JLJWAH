import pygame

'''
Library of all functions. Does not include class methods; use 'import classes' to access those methods.
To access the functions here in another file, use 'import functions'.

- Joza, Amie, Jayden: Intro to Programming Fall 2024
'''

def quitCheck(event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            pygame.quit()
    
    if event.type == pygame.QUIT:
        pygame.quit()

def moveCheck(event,player,player2):
    # Reset some important values
    player.falling = True
    player2.falling = True
    
    if event.type == pygame.KEYDOWN: # WASD / arrow keys
        # Player
        if event.key == pygame.K_w and player.doubleJump < 2: # move up
            player.jumping = True
            player.jumpSpeed = 10.0
            player.gravMultiplier = 1
            player.doubleJump += 1
        
        if event.key == pygame.K_a: # move left
            player.movingLeft = True

        if event.key == pygame.K_d: # move right
            player.movingRight = True        

        # player2
        if event.key == pygame.K_UP and player2.doubleJump < 2: # move up
            player2.jumping = True
            player2.jumpSpeed = 10.0
            player2.gravMultiplier = 1
            player2.doubleJump += 1

        if event.key == pygame.K_LEFT: # move left
            player2.movingLeft = True

        if event.key == pygame.K_RIGHT: # move right
            player2.movingRight = True
  
    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_a:
            player.movingLeft = False
         
        if event.key == pygame.K_d:
            player.movingRight = False    

        if event.key == pygame.K_LEFT:
            player2.movingLeft = False

        if event.key == pygame.K_RIGHT:
            player2.movingRight = False

    if event.type == pygame.MOUSEBUTTONUP:
        print(str(pygame.mouse.get_pos()[0]) + "," + str(pygame.mouse.get_pos()[1]))
        print(str(player.x)+","+str(player.y))

def attackCheck(event,player,player2):
    if event.type == pygame.KEYDOWN:
        movesP = player.chosenCharacter.moves
        for move in movesP:
            if move == 'melee':
                if event.key == pygame.K_x:
                    player.move2Activated = not player.move2Activated
                    player.move2 = 'melee'
            elif move == 'ranged':
                if event.key == pygame.K_c:
                    player.move3Activated = not player.move3Activated
                    player.move3 = 'ranged'
            elif move == 'support': # more moves to come
                if event.key == pygame.K_z:
                    player.move1Activated = True
                    player.move1 = 'support'
            elif move == 'ult':
                if event.key==pygame.K_v and player.ultUse:
                    player.move4Activated = True
                    player.move4 = 'ult'
                    player.doSaveHP = True
            else:
                player.move1Activated = False

        movesE = player2.chosenCharacter.moves
        for move in movesE:
            if move == 'melee': # moves to come  
                if event.key == pygame.K_m:
                    player2.move2Activated = not player2.move2Activated
                    player2.move2 = 'melee'
            elif move == 'ranged': # moves to come
                if event.key == pygame.K_COMMA:
                    player2.move3Activated = not player2.move3Activated
                    player2.move3 = 'ranged'
            elif move == 'support': # more moves to come
                if event.key == pygame.K_n:
                    player2.move1Activated = True
                    player2.move1 = 'support'
            elif move == 'ult':
                if event.key==pygame.K_PERIOD and player2.ultUse:
                    player2.move4Activated = not player2.move4Activated
                    player2.move4 = 'ult'
                    player2.doSaveHP = True
            else:
                player.move1Activated = False
