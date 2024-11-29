import pygame

'''
Library of all classes, properties, and methods. To access the classes here in another file, use 'import classes'.

- Joza, Amie, Jayden: Intro to Programming Fall 2024
'''

class Entity:
    def __init__(self,x,y,imagePath,speed):        
        loaded = pygame.image.load(imagePath)
        self.image = pygame.transform.scale(loaded, (50, 60))
        self.sizex = self.image.get_size()[0]
        self.sizey = self.image.get_size()[1]

        self.x = x
        self.y = y
        
        self.gravity = 2.0
        self.gravMultiplier = 1
        self.gravInterval = 0.5
        self.jumpSpeed = 20.0 # CHANGE THIS to change speed
        # self.farx = self.x + self.sizex
        # self.fary = self.y + self.sizey        
        self.speed = speed

        self.movingLeft = False
        self.movingRight = False
        self.jumping = False
        self.falling = True

    def update(self,surface,character):
        resX = surface.get_size()[0]
        resY = surface.get_size()[1]
        
        if character.movingLeft and character.x >= 0: # Movement logic - without this, it will only move once when pressed and not when pressed down
            character.x -= character.speed
        if character.movingRight and character.x + character.sizex <= resX: # characterImg.get_size()[0] gets the horizontal size of the character
            character.x += character.speed
        if character.falling and character.y >= 0 and character.y <= resY:
            character.y += character.gravity * self.gravMultiplier
            self.gravMultiplier += self.gravInterval
        if character.jumping and character.y + character.sizey <= resY:
            if self.jumpSpeed > 0:
                character.y -= self.jumpSpeed
            else:
                character.jumping = False

        surface.blit(self.image, (self.x, self.y))

class Player(Entity):
    def __init__(self,x,y,imagePath):
        super().__init__(x,y,imagePath,5.0)
        self.direction = False # facing right
    
class Enemy(Entity):
    def __init__(self,x,y,imagePath):
        super().__init__(x,y,imagePath,2.5)
        self.direction = True # facing left


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

        def solidify(self,surface,character):
            resX = surface.get_size()[0]
            resY = surface.get_size()[1]
            
            '''
            Note: error observed: moving left or right and then hitting the barrier going up or down causes the character to teleport
            '''
            if character.movingLeft and character.x >= 0: # Movement logic - without this, it will only move once when pressed and not when pressed down
                if (not (character.x > self.x1 and character.x < self.x2 and character.y > self.y1-character.sizey and character.y < self.y2)): # Top platform/example
                    character.movingLeft = True # if not hitting a barrier, keep movingLeft as true to move the character
                elif character.x > self.x1 and character.x <= self.x2 and character.y > self.y1-character.sizey and character.y < self.y2:
                    character.x = self.x2+1 # if hitting a barrier, move it outside of the barrier and keep movingLeft as false to stop moving into the barrier
                    character.movingLeft = False
            if character.movingRight and character.x + character.sizex <= resX: # characterImg.get_size()[0] gets the horizontal size of the character
                if (not (character.x + character.sizex > self.x1 and character.x < self.x2 and character.y > self.y1-character.sizey and character.y < self.y2)):
                    character.movingRight = True
                elif character.x < self.x2 and character.x + character.sizex >= self.x1 and character.y > self.y1-character.sizey and character.y < self.y2:
                    character.x = (self.x1-1)-character.sizex
                    character.movingRight = False
            if character.jumping and character.y >= 0:
                if (not (character.y > self.y1 and character.y < self.y2 and character.x > self.x1-character.sizex and character.x < self.x2)):
                    character.jumping = True
                elif character.y <= self.y2 and character.y > self.y1 and character.x > self.x1-character.sizex and character.x < self.x2:
                    character.y = self.y2+1
                    character.jumpSpeed = -1
            if character.falling and character.y + character.sizey <= resY:
                if (not (character.y + character.sizey > self.y1 and character.y < self.y2 and character.x > self.x1-character.sizex and character.x < self.x2)):
                    character.falling = True
                elif character.y < self.y2 and character.y + character.sizey >= self.y1 and character.x > self.x1-character.sizex and character.x < self.x2:
                    character.y = (self.y1-1)-character.sizey
                    character.jumpSpeed = -1
                    character.gravMultiplier = 1
                    character.falling = False

        '''
        ### Example code for a barrier with topleft corner (550,102) and bottomRight corner (733,124):


        if character.movingLeft and character.x >= 0: # Movement logic - without this, it will only move once when pressed and not when pressed down
            if (not (character.x > 550 and character.x < 733 and character.y > 102-character.sizey and character.y < 124)): # Top platform/example
                character.x -= character.speed
                if character.x > 550 and character.x <= 733 and character.y > 102-character.sizey and character.y < 124:
                    character.x = 733
        if character.movingRight and character.x + character.sizex <= resX: # characterImg.get_size()[0] gets the horizontal size of the character
            if (not (character.x + character.sizex > 550 and character.x < 733 and character.y > 102-character.sizey and character.y < 124)):
                character.x += character.speed
                if character.x < 733 and character.x + character.sizex >= 550 and character.y > 102-character.sizey and character.y < 124:
                    character.x = 550-character.sizex
        if character.jumping and character.y >= 0:
            if (not (character.y > 102 and character.y < 124 and character.x > 550-character.sizex and character.x < 733)):
                character.y -= character.speed
                if character.y <= 124 and character.y > 102 and character.x > 550-character.sizex and character.x < 733:
                    character.y = 125
        if character.falling and character.y + character.sizey <= resY:
            if (not (character.y + character.sizey > 102 and character.y < 124 and character.x > 550-character.sizex and character.x < 733)):
                character.y += character.speed
                if character.y < 124 and character.y + character.sizey >= 102 and character.x > 550-character.sizex and character.x < 733:
                    character.y = 101-character.sizey
        '''


class Move:
    def __init__(self,sentFrom):
        self.character = sentFrom
        self.x = self.character.x
        self.y = self.character.y

        
class Attack(Move):
    def __init__(self,sentFrom,damage):
        super.__init__(sentFrom)
        self.dmg = damage
        self.direction = True # True = facing Left, False = Right. Computed property with code yet to follow.

class Melee(Attack):
    def __init__(self,sentFrom,damage):
        super().__init__(sentFrom,damage)

class Ranged(Attack):
    def __init__(self,sentFrom,damage):
        super().__init__(sentFrom,damage)

    class Projectile:
        def __init(self,animationDirectory,speed):
            self.speed = speed
            self.images = []
            
            for image in animationDirectory:
                loaded = pygame.image.load(image)
                self.images.append(loaded)
        

class Defense(Move):
    def __init__(self,sentFrom,health):
        super.__init__(sentFrom)
        self.hp = health
        self.isActive = False # defense unactivated by default, only activated when button is pressed.
