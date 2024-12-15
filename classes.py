import pygame

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
        self.ultUse=True
        self.gravity = 2.0
        self.gravMultiplier = 1
        self.gravInterval = 0.1
        self.jumpSpeed = 10.0 # CHANGE THIS to change speed (& don't forget to change it in functions.py!)
        # self.farx = self.x + self.sizex
        # self.fary = self.y + self.sizey        
        self.speed = speed
        self.nuke= False
        self.direction = True # True = facing left, False = facing right

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
        
            #put color here

        # Animation
        # Left
        if character.movingLeft:
            character.direction = True
            character.chosenCharacter.last_left+=1
            if character.chosenCharacter.last_left == len(character.chosenCharacter.imagePaths)/2:
                character.chosenCharacter.last_left = 0
            character.image = character.chosenCharacter.images[character.chosenCharacter.last_left]
        else:
            character.chosenCharacter.last_left = 0
        #Right
        if character.movingRight: 
            character.direction = False
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
            self.move2Activated = False
        if self.move3Activated:
            dmg = moves[self.move3][0].execute(character,enemy)
            self.hp += dmg
        if self.move4Activated: # and self.hp > 100.0
            if moves[self.move4][0].isActive:
                moves[self.move4][0].execute(character)
        if self.nuke:
            self.hp+=100.0
            enemy.hp+=100.0

        if self.attackHit == True:
            if self.x > enemy.x:
                self.hitFrom = "left"
            if self.x < enemy.x:
                self.hitFrom = "right"
        if self.hitFrom == "left" and self.attackHit == True:
            self.knockBackMultiplier = (self.hp/100.0)+1.0
            self.x+= self.knockback*(self.knockBackMultiplier*0.75)+1.0
            self.y-= self.knockback*self.knockBackMultiplier+1.0
            self.attackHit = False
        if self.hitFrom == "right" and self.attackHit == True:
            self.knockBackMultiplier = (self.hp/100.0)+1.0
            self.x-= self.knockback*(self.knockBackMultiplier*0.75)+1.0
            self.y-= self.knockback*self.knockBackMultiplier+1.0
            self.attackHit = False
        
        if enemy.attackHit == True:
            if enemy.x > self.x:
                enemy.hitFrom = "left"
            if enemy.x < self.x:
                enemy.hitFrom = "right"
        if enemy.hitFrom == "left" and enemy.attackHit == True:
            enemy.knockBackMultiplier = (enemy.hp/100.0)+1.0
            enemy.x+= enemy.knockback*(enemy.knockBackMultiplier*0.75)+100.0
            enemy.y-= enemy.knockback*enemy.knockBackMultiplier+100.0
            enemy.attackHit = False
        if enemy.hitFrom == "right" and enemy.attackHit == True:
            enemy.knockBackMultiplier = (enemy.hp/100)+1.0
            enemy.x-= enemy.knockback*(enemy.knockBackMultiplier*0.75)+100.0
            enemy.y-= enemy.knockback*enemy.knockBackMultiplier+100.0
            enemy.attackHit = False

        surface.blit(self.image, (self.x, self.y))

class Player(Entity):
    def __init__(self,x,y,chosenCharacter):
        super().__init__(x,y,chosenCharacter.imagePaths[0],2.0,chosenCharacter)
        self.direction = False # facing right
        self.chosenCharacter = chosenCharacter

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
                character.y = 300
                character.gravMultiplier = 0
                enemy.score += 1


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
    def __init__(self,sentFrom):
        super().__init__(sentFrom)

class Melee(Attack):
    def __init__(self,sentFrom):
        super().__init__(sentFrom)
        self.hitboxWidth = 25
        self.hitboxHeight = 10
        self.damage = 5.0

class Ranged(Attack):
    def __init__(self,sentFrom):
        super().__init__(sentFrom)
        self.projectileSpeed = 10
        self.projectileX = self.x
        self.projectileY = self.y
        self.projectileSizeX = 10
        self.projectileSizeY = 15
        self.damage = 10.0
        

class Ult(Attack):
    def __init__(self,sentFrom):
        super().__init__(sentFrom)

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
        self.sizex = self.照片.get_size()[0]
        self.sizey = self.照片.get_size()[1]
    def execute(self,sentFrom,enemy):
        self.enemy = enemy
        self.character = sentFrom

        self.x = self.照片.get_rect().x
        self.y = self.照片.get_rect().y
        self.hitboxWidth = 100
        self.hitboxHeight = 200
        if enemy.y>self.character.y-self.hitboxHeight and enemy.y<self.character.y+self.hitboxHeight:
            if self.character.direction == True:
                if enemy.x>self.character.x-self.hitboxWidth and enemy.x<self.character.x:
                    enemy.attackHit = True  
                    enemy.hp+=self.damage*(enemy.hp/100+1.0)
                    print(enemy.attackHit)
            if self.character.direction == False:
                if enemy.x<self.character.x+self.hitboxWidth and enemy.x>self.character.x:
                    enemy.attackHit = True
                    enemy.hp +=self.damage*(enemy.hp/100+1.0)
                    print(enemy.attackHit)

        if self.character.direction == False: # Facing right
            self.surface.blit(self.照片,(self.character.x + self.character.sizex,self.character.y + self.character.sizey/2-(self.sizey/2))) # publish the image in front of player and at the center
        else:
            flipped = pygame.transform.flip(self.照片,True,False)
            self.surface.blit(flipped,(self.character.x - self.sizex,self.character.y + self.character.sizey/2-(self.sizey/2)))
        
        pygame.draw.rect(self.surface,'red',((self.x-self.hitboxWidth),(self.y-self.hitboxHeight),(self.x),(self.y+self.hitboxHeight)),3)
        print(enemy.attackHit)
        return self.damage
        
    
class Fireball(Ranged): 
    def __init__(self,surface,damage):
        self.damage = damage
        self.surface = surface
        a = 'a'; self.照片 = pygame.image.load(f"assets\{a}ttacks\Mario\Mario_fireball.png")

#taco moment
    def execute(self,sentFrom,enemy):     
        super().__init__(sentFrom)   
        self.enemy = enemy
        self.character = sentFrom
        self.projectileSizeX = 100
        self.projectileSizeY = 100
        self.projectileSpeed = 10
        self.projectileX
        self.projectileY
        if enemy.y>self.projectileY-self.projectileSizeY and enemy.y<self.projectileY+self.projectileSizeY:
            if self.character.direction == True:
                if enemy.x>self.projectileX-self.projectileSizeX and enemy.x<self.projectileX:
                    enemy.attackHit = True  
                    enemy.hp+=self.damage*(enemy.hp/100+1.0)
                    print(enemy.attackHit)
            if self.character.direction == False:
                if enemy.x<self.projectileX+self.projectileSizeX and enemy.x>self.projectileX:
                    enemy.attackHit = True
                    enemy.hp +=self.damage*(enemy.hp/100+1.0)
                    print(enemy.attackHit)
        if self.character.direction == True:
            while self.projectileSizeX>0:
                self.projectileX-=self.projectileSpeed
            self.projectileSizeX=-100
            self.projectileSizeY=-100
        if self.character.direction == False:
            while self.projectileSizeX<1280:
                self.projectileX-=self.projectileSpeed
            self.projectileSizeX=-100
            self.projectileSizeY=-100

        

        self.surface.blit(self.照片,(self.projectileX,self.projectileY)) # zhao pian W
        return self.damage


class Knives(Ranged): 
    def __init__(self,surface,damage):
        self.damage = damage
        self.surface = surface
        a = 'a'; self.照片 = pygame.image.load(f"assets\{a}ttacks\Mario\Mario_fireball.png") #update to fit image
#taco moment
    def execute(self,sentFrom,enemy):
        self.enemy = enemy
        self.character = sentFrom
        self.surface.blit(self.照片,(self.projectileX,self.projectileY)) # zhao pian W

class Shield(Defense):
    def __init__(self,surface):
        self.hp = 50
        self.surface = surface

    def execute(self,sentFrom):
        self.character = sentFrom
        pygame.draw.circle(self.surface,'white',(self.character.x+(self.character.sizex/2),self.character.y+(self.character.sizey/2)),50,5)

class Nuke(Ult):
    def __init__(self,damage,attackHit,enemy):
        self.x = self.character.x
        self.y = self.character.y
        self.damage = 100
        self.attackHit = True
        enemy.attackHit = True

class Vent(Ult):
    def __init__(self,surface):
        self.tick = 0
        self.isActive = True
        self.surface = surface
        self.saveImages = True        

    def execute(self,sentFrom):
        if self.saveImages:
            self.tempCharImages = sentFrom.chosenCharacter.images
        self.images = []
        v='v';image = pygame.image.load(f"assets\characters\AmongUs\{v}ent.jpg")
        for i in range(9):
            self.images.append(image)
        sentFrom.chosenCharacter.images = self.images

        if self.tick < 10*60: # 10 seconds * 60 frames per second
            self.tick += 1
            print(self.tick)
        if self.tick == 600:
            self.isActive = False


# Character class (not entity!)
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
