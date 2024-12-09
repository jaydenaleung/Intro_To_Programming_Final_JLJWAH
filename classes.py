import pygame
import time

'''
Library of all classes, properties, and methods. To access the classes here in another file, use 'import classes'.

- Joza, Amie, Jayden: Intro to Programming Fall 2024
'''

class Entity:
    def __init__(self,x,y,imagePath,speed,sentFrom):        
        loaded = pygame.image.load(imagePath)
        self.image = pygame.transform.scale(loaded, (30, 40))
        self.sizex = self.image.get_size()[0]
        self.sizey = self.image.get_size()[1]

        self.x = x
        self.y = y
        
        self.gravity = 2.0
        self.gravMultiplier = 1
        self.gravInterval = 0.1
        self.jumpSpeed = 10.0 # CHANGE THIS to change speed (& don't forget to change it in functions.py!)
        # self.farx = self.x + self.sizex
        # self.fary = self.y + self.sizey        
        self.speed = speed

        self.hp = 0.0 #hp
        self.score = 0

        self.movingLeft = False
        self.movingRight = False
        self.jumping = False
        self.falling = True

        self.doubleJump = 0
        self.attackHit = False
        self.hitFrom = "None"
        self.knockback = 10
        self.knockBackMultiplier = (self.hp/100)+1.0

        self.move1 = ''
        self.move1Activated = False
        self.move2 = ''
        self.move2Activated = False
        self.move3 = ''
        self.move3Activated = False
        self.move4 = ''
        self.move4Activated = False

    def update(self,surface,character,characters):
        resX = surface.get_size()[0]
        resY = surface.get_size()[1]

        enemy = [c for c in characters if c != character][0] # determine enemy

        moves = character.chosenCharacter.moves
        
        # Render movement
        if character.movingLeft and character.x >= 0: # Movement logic - without this, it will only move once when pressed and not when pressed down
            character.x -= character.speed
        if character.movingRight and character.x + character.sizex <= resX: # characterImg.get_size()[0] gets the horizontal size of the character
            character.x += character.speed
        if character.falling and character.y >= 0 and character.y <= resY:
            character.y += character.gravity * self.gravMultiplier
            self.gravMultiplier += self.gravInterval
        if character.jumping and character.y + character.sizey <= resY:
            if self.jumpSpeed > 0 and not self.doubleJump:
                character.y -= self.jumpSpeed
            if self.jumpSpeed > 0 and self.doubleJump:
                character.y -= self.jumpSpeed
            else:
                character.jumping = False

        # Animation
        # Left
        if character.movingLeft: 
            character.chosenCharacter.last_left+=1
            if character.chosenCharacter.last_left == len(character.chosenCharacter.imagePaths)/2:
                character.chosenCharacter.last_left = 0
            character.image = character.chosenCharacter.images[character.chosenCharacter.last_left]
        else:
            character.chosenCharacter.last_left = 0
        #Right
        if character.movingRight: 
            character.chosenCharacter.last_right+=1
            if character.chosenCharacter.last_right == len(character.chosenCharacter.imagePaths):
                character.chosenCharacter.last_right = int(len(character.chosenCharacter.imagePaths)/2)
            character.image = character.chosenCharacter.images[character.chosenCharacter.last_right]
        else:
            character.chosenCharacter.last_right = int(len(character.chosenCharacter.imagePaths)/2)
        
        # Render attacks
        if self.move1Activated:
            moves[self.move1][0].execute(character)
        if self.move2Activated:
            dmg = moves[self.move2][0].execute(character,enemy)
            self.hp += dmg
        if self.move3Activated:
            dmg = moves[self.move3][0].execute(character,enemy)
            self.hp += dmg
        if self.move4Activated:
            pass

        if self.attackHit == True:
            if self.x > enemy.x:
                self.hitFrom == "left"
            if self.x < enemy.x:
                self.hitFrom == "right"
        if self.hitFrom == "left":
            self.knockBackMultiplier = (self.hp/100)+1.0
            self.x+= self.knockback*(self.knockBackMultiplier*0.75)
            self.y+= self.knockback*self.knockBackMultiplier
        if self.hitFrom == "right":
            self.knockBackMultiplier = (self.hp/100)+1.0
            self.x-= self.knockback*(self.knockBackMultiplier*0.75)
            self.y+= self.knockback*self.knockBackMultiplier

        surface.blit(self.image, (self.x, self.y))

class Player(Entity):
    def __init__(self,x,y,chosenCharacter):
        super().__init__(x,y,chosenCharacter.imagePaths[0],2.0,chosenCharacter)
        self.direction = False # facing right
        self.chosenCharacter = chosenCharacter
        self.knockbackMultiplier = self.hp/2
        if self.attackHit == True:
            pass
            #knockback code here

    
class Enemy(Entity):
    def __init__(self,x,y,chosenCharacter):
        super().__init__(x,y,chosenCharacter.imagePaths[9],2.0,chosenCharacter)
        self.direction = True # facing left
        self.chosenCharacter = chosenCharacter

class Scene:
    def __init__(self,imagePath):
        self.image = pygame.image.load(imagePath)
        self.barriers = []
        self.spawnX1 = 0
        self.spawnY1 = 0
        self.spawnX2 = 0
        self.spawnY2 = 0

    def update(self,screen):
        screen.blit(self.image,(0,0))

    class Barrier: # nested class means the Scene class must be initialized before the Barrier class
        def __init__(self,x1,y1,x2,y2):
            self.x1 = x1 # topLeft corner
            self.y1 = y1 # topLeft corner
            self.x2 = x2 # bottomRight corner
            self.y2 = y2 # bottomRight corner

        def solidify(self,surface,character,characters):
            resX = surface.get_size()[0]
            resY = surface.get_size()[1]
            enemy = [c for c in characters if c != character][0] # determine enemy

            '''
            Note: error observed: moving left or right and then hitting the barrier going up or down causes the character to teleport
            '''
            
            if character.x < 0 or character.x + character.sizex > resX or character.y < 0 or character.y + character.sizey > resY: # respawn
                character.x = 640
                character.y = 100
                character.gravMultiplier = 0
                enemy.score += 1
                time.sleep(3) # wait 3 secs


            if character.jumping and character.y >= 0:
                if (not (character.y > self.y1 and character.y < self.y2 and character.x > self.x1-character.sizex and character.x < self.x2)):
                    character.jumping = True
                elif character.y <= self.y2 and character.y >= self.y1 and character.x > self.x1-character.sizex and character.x < self.x2:
                    character.y = self.y2+1
                    character.jumpSpeed = -1
                    character.gravMultiplier = 1
            if character.falling and character.y + character.sizey <= resY:
                if (not (character.y + character.sizey > self.y1 and character.y < self.y2 and character.x > self.x1-character.sizex and character.x < self.x2)):
                    character.falling = True
                elif character.y <= self.y2 and character.y + character.sizey >= self.y1 and character.x > self.x1-character.sizex and character.x < self.x2:
                    character.y = (self.y1-1)-character.sizey
                    character.jumpSpeed = -1
                    character.gravMultiplier = 1
                    character.doubleJump = 0
                    character.falling = False
            if character.movingLeft and character.x >= 0: # Movement logic - without this, it will only move once when pressed and not when pressed down
                if (not (character.x > self.x1 and character.x < self.x2 and character.y > self.y1-character.sizey and character.y < self.y2)): # Top platform/example
                    character.movingLeft = True # if not hitting a barrier, keep movingLeft as true to move the character
                elif character.x >= self.x1 and character.x <= self.x2 and character.y > self.y1-character.sizey+1 and character.y < self.y2:
                    character.x = self.x2+1 # if hitting a barrier, move it outside of the barrier and keep movingLeft as false to stop moving into the barrier
                    character.movingLeft = False
            if character.movingRight and character.x + character.sizex <= resX: # characterImg.get_size()[0] gets the horizontal size of the character
                if (not (character.x + character.sizex > self.x1 and character.x < self.x2 and character.y > self.y1-character.sizey and character.y < self.y2)):
                    character.movingRight = True
                elif character.x <= self.x2 and character.x + character.sizex >= self.x1+1 and character.y > self.y1-character.sizey+1 and character.y < self.y2:
                    character.x = (self.x1-1)-character.sizex
                    character.movingRight = False
            
                    
class Move:
    def __init__(self,sentFrom):
        self.character = sentFrom
        self.x = self.character.x
        self.y = self.character.y
        
class Attack(Move):
    def __init__(self,sentFrom,enemy,damage):
        super().__init__(sentFrom)
        self.hitboxWidth = 100
        self.hitboxHeight = 200
        self.direction = True # True = facing Left, False = Right. Computed property with code yet to follow.
        if self.direction == True:
            hitbox = [self.x-self.hitboxWidth,self.y+self.hitboxHeight/2,self.y-self.hitboxHeight/2]  
        elif self.direction == False:
            hitbox = [self.x+self.hitboxWidth/2,self.y+self.hitboxHeight/2,self.y-self.hitboxHeight/2]
        if enemy.y>hitbox[2] and enemy.y<hitbox[1]:
            if self.direction == True:
                if enemy.x>hitbox[0] and enemy.x<self.x:
                    enemy.attackHit = True
                    enemy.hp+=self.damage*(enemy.hp/100,0+1.0)
            if self.direction == False:
                if enemy.x<hitbox[0] and enemy.x>self.x:
                    enemy.attackHit = True
                    enemy.attackHit +=self.damage*(enemy.hp/100,0+1.0)

class Melee(Attack):
    def __init__(self,sentFrom):
        super().__init__(sentFrom)
        self.hitboxWidth = 25
        self.hitboxHeight = 10
        self.damage = 5.0

class Ranged(Attack):
    def __init__(self,sentFrom,damage):
        super().__init__(sentFrom,damage)
    def execute(self,enemy):
        self.projectileSpeed = 10
        self.projectileX = self.x
        self.projectileY = self.y
        self.projectileSizeX = 10
        self.projectileSizeY = 15
        self.damage = 10
        if not self.direction:
            while self.projectileX < 1280 and not ((self.projectileX+self.projectileSizeX or self.projectileX-self.projectileSizeX) and (self.projectileY+self.projectileSizeY or self.projectileY-self.projectileSizeY) == enemy.x):
                self.projectileX += self.projectileSpeed
            if self.projectileX == enemy.x:
                enemy.attackHit = True  
                self.projectileX = -100
                self.projectileY = -100
        if self.direction:
            while self.projectileX > 0 and not ((self.projectileX+self.projectileSizeX or self.projectileX-self.projectileSizeX) and (self.projectileY+self.projectileSizeY or self.projectileY-self.projectileSizeY) == enemy.x):
                self.projectileX -= self.projectileSpeed
            if self.projectileX == enemy.x:
                enemy.attackHit = True
                self.projectileX = -100
                self.projectileY = -100

class Support(Move):
    def __init__(self):
        pass

class Defense(Support):
    def __init__(self):
        pass


### MOVES

class Punch(Melee):
    def __init__(self,surface,damage):
        self.damage = damage
        self.surface = surface
        a = 'a'; self.照片 = pygame.image.load(f"assets\{a}ttacks\Mario\Mario_punch.png")
    def execute(self,sentFrom,enemy):
        self.enemy = enemy
        self.character = sentFrom
        self.surface.blit(self.照片,(self.character.x + self.character.sizex,self.character.y + self.character.sizey/2-(self.照片.get_size()[1])/2)) # publish the image in front of player and at the center
    
class Fireball(Ranged): 
    def __init__(self,surface,damage):
        self.damage = damage
        self.surface = surface
        a = 'a'; self.照片 = pygame.image.load(f"assets\{a}ttacks\Mario\Mario_fireball.png")
#taco moment
    def execute(self,sentFrom,enemy):
        self.enemy = enemy
        self.character = sentFrom
        self.surface.blit(self.照片,(self.projectileX,self.projectileY)) # zhao pian W


class Shield(Defense):
    def __init__(self,surface):
        self.hp = 50
        self.isActive = False # defense unactivated by default, only activated when button is pressed.
        self.surface = surface

    def execute(self,sentFrom):
        self.character = sentFrom
        pygame.draw.circle(self.surface,'white',(self.character.x+(self.character.sizex/2),self.character.y+(self.character.sizey/2)),50,5)


class Character:
    def __init__(self,imagePaths=[str],moves=[]):
        self.imagePaths = imagePaths
        self.images = []
        for image in self.imagePaths: # loading each animation frame
            loaded = pygame.image.load(image)
            addImage = pygame.transform.scale(loaded, (30,40))
            self.images.append(addImage)

        self.last_left = 0
        self.last_right = 0

        self.melee = []
        self.ranged = []
        self.support = []
        for move in moves: # categorizing the given moves
            if isinstance(move,Melee):
                self.melee.append(move)
            elif isinstance(move,Ranged):
                self.ranged.append(move)
            elif isinstance(move,Support): # else not used to be safe
                self.support.append(move)

        self.moves = {'melee':self.melee,'ranged':self.ranged,'support':self.support} # dictionary of moves (syntax is key: value)
