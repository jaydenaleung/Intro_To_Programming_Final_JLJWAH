import pygame

# Start Pygame
pygame.init()
resX = 1280; resY = 720
screen = pygame.display.set_mode((resX, resY))
clock = pygame.time.Clock()
running = True
pygame.display.set_caption("Intro to Programming")

# Background
background = "white"

# Example player
playerImg = pygame.image.load("example_player.png")
playerX = 300
playerY = 300
playerMovementIncrement = 5.0
movingLeft = False
movingRight = False
movingUp = False
movingDown = False

def player(x,y):
    screen.blit(playerImg, (x, y))

while running:
    # SETUP
    screen.fill(background)


    # WATCH FOR EVENTS HERE (CONDITIONALS SECTION)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN: # WASD / arrow keys
            if event.key == pygame.K_LEFT or event.key == pygame.K_a: # move left
                movingLeft = True

            if event.key == pygame.K_RIGHT or event.key == pygame.K_d: # move right
                movingRight = True
            
            if event.key == pygame.K_UP or event.key == pygame.K_w: # move up
                movingUp = True
            
            if event.key == pygame.K_DOWN or event.key == pygame.K_s: # move down
                movingDown = True
        elif event.type == pygame.KEYUP:
            movingLeft = False
            movingRight = False
            movingUp = False
            movingDown = False
    
    if movingLeft and playerX >= 0: # Movement logic - without this, it will only move once when pressed and not when pressed down
        playerX -= playerMovementIncrement
    if movingRight and playerX + playerImg.get_size()[0] <= resX: # playerImg.get_size()[0] gets the horizontal size of the player
        playerX += playerMovementIncrement
    if movingUp and playerY >= 0:
        playerY -= playerMovementIncrement
    if movingDown and playerY + playerImg.get_size()[1] <= resY:
        playerY += playerMovementIncrement


    # RENDER GAME OBJECTS HERE 
    player(playerX,playerY)
    

    # UPDATE SCREEN
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60

pygame.quit()