import pygame


class Entity:
    def __init__(self,x,y,imagePath,speed):
        self.image = pygame.image.load(imagePath)
        self.sizex = self.image.get_size()[0]
        self.sizey = self.image.get_size()[1]

        self.x = x
        self.y = y
        # self.farx = self.x + self.sizex
        # self.fary = self.y + self.sizey        
        self.speed = speed

        self.movingLeft = False
        self.movingRight = False
        self.movingUp = False
        self.movingDown = False

class Player(Entity):
    def __init__(self,x,y,imagePath):
        super().__init__(x,y,imagePath,5.0)
        
    def update(self,surface):
        surface.blit(self.image, (self.x, self.y))

class Enemy(Entity):
    def __init__(self,x,y,imagePath):
        super().__init__(x,y,imagePath,2.5)
        
    def update(self,surface):
        surface.blit(self.image, (self.x, self.y))

class Scene:
    def __init__(self,imagePath):
        self.image = pygame.image.load(imagePath)

    def update(self,screen):
        screen.blit(self.image,(0,0))

    class Barrier: # nested class means the Scene class must be initialized before the Barrier class
        def __init__(self,x1,y1,x2,y2):
            self.x1 = x1 # topLeft corner
            self.y1 = y1 # topLeft corner
            self.x2 = x2 # bottomRight corner
            self.y2 = y2 # bottomRight corner

        def solidify(self,player,resX,resY):
            if player.movingLeft and player.x >= 0: # Movement logic - without this, it will only move once when pressed and not when pressed down
                if (not (player.x > self.x1 and player.x < self.x2 and player.y > self.y1-player.sizey and player.y < self.y2)): # Top platform/example
                    player.x -= player.speed
                    if player.x > self.x1 and player.x <= self.x2 and player.y > self.y1-player.sizey and player.y < self.y2:
                        player.x = self.x2+1
            if player.movingRight and player.x + player.sizex <= resX: # playerImg.get_size()[0] gets the horizontal size of the player
                if (not (player.x + player.sizex > self.x1 and player.x < self.x2 and player.y > self.y1-player.sizey and player.y < self.y2)):
                    player.x += player.speed
                    if player.x < self.x2 and player.x + player.sizex >= self.x1 and player.y > self.y1-player.sizey and player.y < self.y2:
                        player.x = (self.x1-1)-player.sizex
            if player.movingUp and player.y >= 0:
                if (not (player.y > self.y1 and player.y < self.y2 and player.x > self.x1-player.sizex and player.x < self.x2)):
                    player.y -= player.speed
                    if player.y <= self.y2 and player.y > self.y1 and player.x > self.x1-player.sizex and player.x < self.x2:
                        player.y = self.y2+1
            if player.movingDown and player.y + player.sizey <= resY:
                if (not (player.y + player.sizey > self.y1 and player.y < self.y2 and player.x > self.x1-player.sizex and player.x < self.x2)):
                    player.y += player.speed
                    if player.y < self.y2 and player.y + player.sizey >= self.y1 and player.x > self.x1-player.sizex and player.x < self.x2:
                        player.y = (self.y1-1)-player.sizey

        '''
        ### Example code for a barrier with topleft corner (550,102) and bottomRight corner (733,124):


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
        '''
