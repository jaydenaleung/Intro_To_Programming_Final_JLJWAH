import pygame
import time

'''
Library of all classes, properties, and methods. To access the classes here in another file, use 'import classes'.

- Joza, Amie, Jayden: Intro to Programming Fall 2024
'''

class Entity: # default class for playable character
    def __init__(self,x,y,speed,chosenCharacter):        
        self.chosenCharacter = chosenCharacter
        
        self.image = self.chosenCharacter.images[0]
        self.sizex = self.image.get_size()[0]
        self.sizey = self.image.get_size()[1]

        self.x = x
        self.y = y
        self.gravity = 2.0
        self.gravMultiplier = 1
        self.gravInterval = 0.1
        self.jumpSpeed = 10.0 # CHANGE THIS to change speed (& don't forget to change it in functions.py!)
        self.speed = speed
        self.direction = True # True = facing left, False = facing right

        self.hp = 0.0 #hp
        self.doSaveHP = False # for amongus vent attack
        self.savedHP = 0.0
        self.score = 0 #amt of times other player has died

        self.movingLeft = False
        self.movingRight = False
        self.jumping = False
        self.falling = True

        self.doubleJump = 0
        self.attackHit = False # refers to when you yourself are hit
        self.hitFrom = "None"
        self.knockback = 20
        self.knockBackMultiplier = (self.hp/100)+1.0

        self.move1 = ''
        self.move1Activated = False
        self.move2 = ''
        self.move2Activated = False
        self.move3 = ''
        self.move3Activated = False
        self.renderNewProj = False
        self.move4 = ''
        self.move4Activated = False
        self.ultUse = False
        self.ultUsed = False

    def update(self,surface,scene,character,characters): 
        resX = surface.get_size()[0]
        resY = surface.get_size()[1]
        self.sizex = self.image.get_size()[0]
        self.sizey = self.image.get_size()[1]

        enemy = [c for c in characters if c != character][0] # determine enemy

        moves = character.chosenCharacter.moves
        if self.hp >= 100.0 and self.ultUsed == False: self.ultUse = True # is the hp above 100 and you haven't used the ult yet? if yes then you can use your ultimate
        else: self.ultUse = False
        
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
        
        # Render attacks
        if self.move1Activated:
            if self.chosenCharacter.support[0].hp != 0: moves[self.move1][0].execute(character)
            else: self.move1Activated = False; self.chosenCharacter.support[0].hp = 5
        if self.move2Activated:
            dmg = moves[self.move2][0].execute(character,enemy)
            if not enemy.move1Activated: enemy.hp += dmg
            else: enemy.chosenCharacter.support[0].hp -= dmg
            self.move2Activated = False
        if self.move3Activated:
            dmg = moves[self.move3][0].execute(character,enemy)
            if not enemy.move1Activated: enemy.hp += dmg
            else: enemy.chosenCharacter.support[0].hp -= dmg
        if self.move4Activated:
            if moves[self.move4][0].isActive:
                moves[self.move4][0].execute(scene,character,enemy)
            if self.doSaveHP:
                print(self.hp)
                self.savedHP = self.hp
                print(self.savedHP)
                self.doSaveHP = False
                
        #knockback and hp logic, includes scaling
        if self.attackHit == True:
            if self.x > enemy.x:
                self.hitFrom = "left"
            if self.x < enemy.x:
                self.hitFrom = "right"
        if self.hitFrom == "left" and self.attackHit == True:
            self.knockBackMultiplier = (self.hp/10.0)+1.0
            self.x+= self.knockback*(self.knockBackMultiplier)+1.0
            self.y-= self.knockback*self.knockBackMultiplier+1.0
            self.attackHit = False
        if self.hitFrom == "right" and self.attackHit == True:
            self.knockBackMultiplier = (self.hp/10.0)+1.0
            self.x-= self.knockback*(self.knockBackMultiplier*0.75)+1.0
            self.y-= self.knockback*self.knockBackMultiplier+1.0
            self.attackHit = False

        #same but for the other player
        if enemy.attackHit == True:
            if enemy.x > self.x:
                enemy.hitFrom = "left"
            if enemy.x < self.x:
                enemy.hitFrom = "right"
        if enemy.hitFrom == "left" and enemy.attackHit == True:
            enemy.knockBackMultiplier = (enemy.hp/10.0)+1.0
            enemy.x+= enemy.knockback*(enemy.knockBackMultiplier)+1.0
            enemy.y-= enemy.knockback*enemy.knockBackMultiplier+1.0
            enemy.attackHit = False
        if enemy.hitFrom == "right" and enemy.attackHit == True:
            enemy.knockBackMultiplier = (enemy.hp/10.0)+1.0
            enemy.x-= enemy.knockback*(enemy.knockBackMultiplier)+1.0
            enemy.y-= enemy.knockback*enemy.knockBackMultiplier+1.0
            enemy.attackHit = False

        # Animation        
        if character.movingLeft:
            character.direction = True
        if character.movingRight: 
            character.direction = False

        if not self.move4Activated and character.movingLeft:
            # Left
            if character.movingLeft:
                character.chosenCharacter.last_left+=1
                if character.chosenCharacter.last_left == len(character.chosenCharacter.imagePaths)/2:
                    character.chosenCharacter.last_left = 0
                character.image = character.chosenCharacter.images[character.chosenCharacter.last_left]
            else:
                character.chosenCharacter.last_left = 0
        elif not self.move4Activated and character.movingRight:
            #Right
            if character.movingRight:
                character.chosenCharacter.last_right+=1
                if character.chosenCharacter.last_right == len(character.chosenCharacter.imagePaths):
                    character.chosenCharacter.last_right = int(len(character.chosenCharacter.imagePaths)/2)
                character.image = character.chosenCharacter.images[character.chosenCharacter.last_right]
            else:
                character.chosenCharacter.last_right = int(len(character.chosenCharacter.imagePaths)/2)
        elif not self.move4Activated and character.direction == True: # set image to still/standing if not moving
            untransformed = character.chosenCharacter.images[0]
            self.image = pygame.transform.scale(untransformed, (30,40))
        elif not self.move4Activated and character.direction == False: # set image to still/standing if not moving
            untransformed = character.chosenCharacter.images[9]
            self.image = pygame.transform.scale(untransformed, (30,40))
        elif character.chosenCharacter.ult[0].__class__.__name__ == "Vent": # venting!
            a='a';v='v';self.image = pygame.image.load(f"assets\{a}ttacks\AmongUs\{v}ent.png")
            self.hp = self.savedHP

        surface.blit(self.image, (self.x, self.y))

class Player(Entity): # class for yourself
    def __init__(self,x,y,chosenCharacter):
        super().__init__(x,y,2.0,chosenCharacter)
        self.direction = False # facing right
        self.chosenCharacter = chosenCharacter

class Enemy(Entity): # class for the other character
    def __init__(self,x,y,chosenCharacter):
        super().__init__(x,y,2.0,chosenCharacter)
        self.direction = True # facing left
        self.chosenCharacter = chosenCharacter

class Scene: # placeholder for the scences in main.py
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
            self.t0 = None

        def solidify(self,surface,scene,character,characters):
            resX = surface.get_size()[0]
            resY = surface.get_size()[1]
            enemy = [c for c in characters if c != character][0] # determine enemy

            
            if character.x < 0 or character.x + character.sizex > resX or character.y < 0 or character.y + character.sizey > resY: # respawn
                character.x = 640
                character.y = 300
                character.hp = 0
                character.gravMultiplier = 0
                enemy.score += 1

                # Make a temporary respawn platform
                barrier_S = scene.Barrier(600,340,680,341)
                scene.barriers.append(barrier_S)
                
                self.t0 = time.time()

            if self.t0 != None: # destroy the respawn platform after 3 secs
                t1 = time.time()
                dt = t1-self.t0
                if dt > 3.0:
                    scene.barriers.pop()
                    self.t0 = None # disable after popping
                    
            # jumping/doublejump/gravity
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

                     
class Move: #defines move
    def __init__(self,sentFrom):
        self.character = sentFrom
        self.x = self.character.x
        self.y = self.character.y
        
class Attack(Move): #defines attacking moves
    def __init__(self,sentFrom):
        super().__init__(sentFrom)

class Melee(Attack): # creates vars for melee atacks
    def __init__(self,sentFrom):
        super().__init__(sentFrom)
        self.hitboxWidth = 25
        self.hitboxHeight = 10
        self.damage = 5.0

class Ranged(Attack): # creates vars for ranged attacks
    def __init__(self,sentFrom):
        super().__init__(sentFrom)
        self.projectileSpeed = 10
        self.projectileX = self.character.x
        self.projectileY = self.character.y
        self.projectileSizeX = 10
        self.projectileSizeY = 15
        self.damage = 10.0
        

class Ult(Attack): # creates ults under attack
    def __init__(self,sentFrom):
        super().__init__(sentFrom)

class Support(Move): # defines a support type of move
    def __init__(self):
        pass

class Defense(Support): # defines a move for sheild, help with organization
    def __init__(self):
        pass


### MOVES

class Punch(Melee): # Punch for Mario
    def __init__(self,surface,damage):
        self.damage = damage
        self.surface = surface
        a = 'a'; self.照片 = pygame.image.load(f"assets\{a}ttacks\Mario\Mario_punch.png") 
        self.sizex = self.照片.get_size()[0]
        self.sizey = self.照片.get_size()[1]
    def execute(self,sentFrom,enemy):
        self.enemy = enemy
        self.character = sentFrom
        global dmg
        dmg = 0

        self.x = self.照片.get_rect().x
        self.y = self.照片.get_rect().y
        self.hitboxWidth = 100
        self.hitboxHeight = 30
        # hitbox logic
        if enemy.y>self.character.y-self.hitboxHeight and enemy.y<self.character.y+self.hitboxHeight:
            if self.character.direction == True:
                if enemy.x>self.character.x-self.hitboxWidth and enemy.x<self.character.x:
                    enemy.attackHit = True  
                    dmg = self.damage*(enemy.hp/100+1.0)
            if self.character.direction == False:
                if enemy.x<self.character.x+self.hitboxWidth and enemy.x>self.character.x:
                    enemy.attackHit = True
                    dmg = self.damage*(enemy.hp/100+1.0)
        #animation logic
        if self.character.direction == False: # Facing right
            self.surface.blit(self.照片,(self.character.x + self.character.sizex,self.character.y + self.character.sizey/2-(self.sizey/2))) # publish the image in front of player and at the center
        else:
            flipped = pygame.transform.flip(self.照片,True,False)
            self.surface.blit(flipped,(self.character.x - self.sizex,self.character.y + self.character.sizey/2-(self.sizey/2)))
        return dmg
        
class Tongue(Melee): # tongue attack from Amoungus
    def __init__(self,surface,damage):
        self.damage = damage
        self.surface = surface
        a = 'a'; self.照片 = pygame.image.load(f"assets\{a}ttacks\AmongUs\Amongus_tongue.png")
        self.sizex = self.照片.get_size()[0]
        self.sizey = self.照片.get_size()[1]
    def execute(self,sentFrom,enemy):
        self.enemy = enemy
        self.character = sentFrom
        global dmg
        dmg = 0

        self.x = self.照片.get_rect().x
        self.y = self.照片.get_rect().y
        self.hitboxWidth = 100
        self.hitboxHeight = 30
        #hitbox logic
        if enemy.y>self.character.y-self.hitboxHeight and enemy.y<self.character.y+self.hitboxHeight:
            if self.character.direction == True:
                if enemy.x>self.character.x-self.hitboxWidth and enemy.x<self.character.x:
                    enemy.attackHit = True  
                    dmg = self.damage*(enemy.hp/100+1.0)
            if self.character.direction == False:
                if enemy.x<self.character.x+self.hitboxWidth and enemy.x>self.character.x:
                    enemy.attackHit = True
                    dmg = self.damage*(enemy.hp/100+1.0)
        #animation logic
        if self.character.direction == False: # Facing right
            self.surface.blit(self.照片,(self.character.x + self.character.sizex-5,self.character.y+5)) # publish the image in front of player and at the center
        else:
            flipped = pygame.transform.flip(self.照片,True,False)
            self.surface.blit(flipped,(self.character.x - self.sizex+5,self.character.y+5))
        return dmg

class Fireball(Ranged): 
    def __init__(self,surface,damage):
        self.damage = damage
        self.surface = surface
        self.projectiles = []

    def initialize(self):
        proj = FireballMove(self.surface,self.damage)
        self.projectiles.append(proj)

    def continuize(self,sentFrom,enemy):
        total = 0
        for proj in self.projectiles:
            dmg = proj.execute(sentFrom,enemy,self.projectiles)
            total += dmg

        return total

    def execute(self,sentFrom,enemy):
        self.character = sentFrom
        self.enemy = enemy
        self.activated = sentFrom.move3Activated
        dmg = 0

        if self.character.renderNewProj:
            self.initialize() # run initialization(makes the fireball)
            self.character.renderNewProj = False
        if len(self.projectiles) > 0:
            dmg = self.continuize(sentFrom,enemy) # run continuation(runs every frame)
        
        return dmg

'''
WHEN YOU PRESS V FOR THE FIRST TIME:
1. Make a new FireballMove object
2. Return total damage

WHEN YOU PRESS V (EXECUTE):
1. Make a new FireballMove object
2. Make sure continuing ones are still going
3. Return total damage

WHEN MOVE IS ACTIVATED BUT NO EXTRA V PRESSES:
1. Make sure continuing ones are still going
2. Return total damage
'''

class FireballMove(Ranged): # mario fire flower fireball
    def __init__(self,surface,damage):
        self.damage = damage
        self.surface = surface
        self.runOnce = True
        a = 'a'; loaded = pygame.image.load(f"assets\{a}ttacks\Mario\Mario_fireball.png")
        self.照片 = pygame.transform.scale(loaded, (35,25))
    #taco moment
    def execute(self,sentFrom,enemy,projectiles):    
        if self.runOnce:
            super().__init__(sentFrom)
            self.enemy = enemy
            self.character = sentFrom
            self.direction = sentFrom.direction
            self.projectileSpeed = 5
            self.projectileX = self.character.x
            self.projectileY = self.character.y
            self.runOnce = False
        
        global dmg
        dmg = 0 # resets dmg counter to be returned

        if self.direction == True: #movement logiv of the projectile
            self.projectileX -= self.projectileSpeed
        else: 
            self.projectileX += self.projectileSpeed

        self.hitboxWidth = 100
        self.hitboxHeight = 30
        #hitbox logic

        if self.projectileX < 0 or self.projectileX > 1280:
            projectiles.remove(self)
            dmg = 0
        if enemy.y>self.projectileY-self.hitboxHeight and enemy.y<self.projectileY+self.hitboxHeight:
            if self.character.direction == True:
                if enemy.x>self.projectileX-self.hitboxWidth and enemy.x<self.projectileX:
                    enemy.attackHit = True
                    localdmg = self.damage*(enemy.hp/100+1.0)
                    projectiles.remove(self)
                    dmg = localdmg
            if self.character.direction == False:
                if enemy.x<self.projectileX+self.hitboxWidth and enemy.x>self.projectileX:
                    enemy.attackHit = True
                    localdmg = self.damage*(enemy.hp/100+1.0)
                    projectiles.remove(self)
                    dmg = localdmg
        # 'animation' logic
        if self.direction == False: # Facing right
            if self.projectileX<1280:
                flipped = pygame.transform.flip(self.照片,True,False)
                self.surface.blit(flipped,(self.projectileX+10,self.projectileY+5))      
        elif self.direction == True:
            if self.projectileX>0:
                self.surface.blit(self.照片,(self.projectileX-10,self.projectileY+5)) # publish the image in front of player and at the center
        
        return dmg


class Knives(Ranged): 
    def __init__(self,surface,damage):
        self.damage = damage
        self.surface = surface
        self.projectiles = []

    def initialize(self):
        proj = KnivesMove(self.surface,self.damage)
        self.projectiles.append(proj)

    def continuize(self,sentFrom,enemy):
        total = 0
        for proj in self.projectiles:
            dmg = proj.execute(sentFrom,enemy,self.projectiles)
            total += dmg

        return total

    def execute(self,sentFrom,enemy):
        self.character = sentFrom
        self.enemy = enemy
        self.activated = sentFrom.move3Activated
        dmg = 0

        if self.character.renderNewProj:
            self.initialize() # run initialization(makes the fireball)
            self.character.renderNewProj = False
        if len(self.projectiles) > 0:
            dmg = self.continuize(sentFrom,enemy) # run continuation(runs every frame)
        
        return dmg

class KnivesMove(Ranged): # mario fire flower fireball
    def __init__(self,surface,damage):
        self.damage = damage
        self.surface = surface
        self.runOnce = True
        a = 'a'; loaded = pygame.image.load(f"assets\{a}ttacks\AmongUs\knife.png")
        self.照片 = pygame.transform.scale(loaded, (35,25))
    #taco moment
    def execute(self,sentFrom,enemy,projectiles):    
        if self.runOnce:
            super().__init__(sentFrom)
            self.enemy = enemy
            self.character = sentFrom
            self.direction = sentFrom.direction
            self.projectileSpeed = 5
            self.projectileX = self.character.x
            self.projectileY = self.character.y
            self.runOnce = False
        
        global dmg
        dmg = 0 # resets dmg counter to be returned

        if self.direction == True: #movement logiv of the projectile
            self.projectileX -= self.projectileSpeed
        else: 
            self.projectileX += self.projectileSpeed

        self.hitboxWidth = 100
        self.hitboxHeight = 30
        #hitbox logic

        if self.projectileX < 0 or self.projectileX > 1280:
            projectiles.remove(self)
            dmg = 0
        if enemy.y>self.projectileY-self.hitboxHeight and enemy.y<self.projectileY+self.hitboxHeight:
            if self.character.direction == True:
                if enemy.x>self.projectileX-self.hitboxWidth and enemy.x<self.projectileX:
                    enemy.attackHit = True
                    localdmg = self.damage*(enemy.hp/100+1.0)
                    projectiles.remove(self)
                    dmg = localdmg
            if self.character.direction == False:
                if enemy.x<self.projectileX+self.hitboxWidth and enemy.x>self.projectileX:
                    enemy.attackHit = True
                    localdmg = self.damage*(enemy.hp/100+1.0)
                    projectiles.remove(self)
                    dmg = localdmg
        # 'animation' logic
        if self.direction == False: # Facing right
            if self.projectileX<1280:
                self.surface.blit(self.照片,(self.projectileX+10,self.projectileY+5))      
        elif self.direction == True:
            if self.projectileX>0:
                flipped = pygame.transform.flip(self.照片,True,False)
                self.surface.blit(flipped,(self.projectileX-10,self.projectileY+5)) # publish the image in front of player and at the center
        
        return dmg

class Shield(Defense): # creates a shield worth 5 hp
    def __init__(self,surface):
        self.hp = 5
        self.surface = surface

    def execute(self,sentFrom):
        self.character = sentFrom
        pygame.draw.circle(self.surface,'white',(self.character.x+(self.character.sizex/2),self.character.y+(self.character.sizey/2)),50,5)

class Nuke(Ult): # Ult for Mario
    def __init__(self,surface,damage):
        self.damage = damage
        self.isActive = True
        a = 'a'; n = 'n'; self.照片 = pygame.image.load(f"assets\{a}ttacks\Mario\{n}uke.png")
        self.surface = surface
        self.dropping = True
        self.runOnce = True
        self.end = False

    def execute(self,scene,sentFrom,enemy):        
        if self.runOnce:
            self.attackHit = True
            self.character = sentFrom
            self.scene = scene
            self.barriers = self.scene.barriers
            self.enemy = enemy # determine enemy
            enemy.attackHit = True
            self.x = self.character.x
            self.sizex = self.照片.get_size()[0]
            self.y = 0
            self.sizey = self.照片.get_size()[1]
            self.runOnce = False

        if self.y + self.sizey < 720 and self.dropping: # nuke drops to ground before blowing up
            self.y += 5
        else:
            self.dropping = False
            a='a';e='e';self.照片 = pygame.image.load(f"assets\{a}ttacks\Mario\{e}xplosion.png") #taco
            self.y = 320
            self.end = True

        self.surface.blit(self.照片, (self.character.x-(self.照片.get_size()[0]/2),self.y))
        # damage and reset ult
        if self.end:
            enemy.hp += 99.9 
            self.isActive = False
            sentFrom.move4Activated = False
            sentFrom.ultUsed = True
            self.end = False

class Vent(Ult): # amoungus vent
    def __init__(self,surface):
        self.tick = 0
        self.isActive = True
        self.surface = surface       

    def execute(self,scene,sentFrom,enemy):
        #timer for the ult(player is invincible during this time)
        if self.tick < 5*60: # 5 seconds * 60 frames per second = 300 frames = run for only 5 seconds
            self.tick += 1
        if self.tick == 300:
            self.isActive = False
            sentFrom.move4Activated = False
            sentFrom.ultUsed = True
            sentFrom.hp = sentFrom.savedHP


# Character class (loads the move anf stuff)
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
        self.ult = []

        for move in moves: # categorizing the given moves
            if isinstance(move,Melee):
                self.melee.append(move)
            elif isinstance(move,Ranged):
                self.ranged.append(move)
            elif isinstance(move,Support): # else not used to be safe
                self.support.append(move)
            elif isinstance(move,Ult): # else not used to be safe
                self.ult.append(move)

        self.moves = {'melee':self.melee,'ranged':self.ranged,'support':self.support,'ult':self.ult} # dictionary of moves (syntax is key: value)
